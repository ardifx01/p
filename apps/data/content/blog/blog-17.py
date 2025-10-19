"""
Blog Post #17: Membangun Bot di .NET dengan Bot Framework SDK
Interpretasi teknis berformat praktis untuk implementasi cepat.
"""

from datetime import datetime
from django.conf import settings

# Blog data for: Membangun Bot di .NET dengan Bot Framework SDK
blog_data = {
    "id": 17,
    "title": """Membangun Bot di .NET dengan Bot Framework SDK""",
    "description": """Langkah lengkap membuat bot di .NET: struktur proyek, adapter, controller, state, dialog, NLU, pengujian, dan deployment.""",
    "images": {
        "dotnet_bot_framework_dark_glow.jpg": f"{settings.BLOG_BASE_IMG_URL}/dotnet_bot_framework_dark_glow.jpg"
    },
    "created_at": datetime.strptime("2025-10-17T20:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "updated_at": datetime.strptime("2025-10-17T20:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "author": "dhiff",
    "username": "dhiff",
    "author_image": f"{settings.BASE_URL}/static/img/pp.jpg",
    "content": [
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": "Artikel ini memandu kamu membangun bot berbasis HTTP di .NET menggunakan Bot Framework SDK: menyiapkan proyek, menulis adapter, controller, logika bot (ActivityHandler), menyimpan percakapan dengan state, membuat dialog, menambah NLU, menguji via Emulator, hingga gambaran deployment."
        },

        { "type": "h2", "class": "text-xl lg:text-2xl text-medium mt-5 mb-3", "text": "Visualisasi Arsitektur" },
        {
            "type": "img",
            "src": f"{settings.BLOG_BASE_IMG_URL}/dotnet_bot_framework_dark_glow.jpg", 
            "class": "rounded-xl border border-zinc-700 my-4 shadow-lg",
            "alt": ".NET Bot Framework — Adapter • State • Dialogs • Channels • LUIS/NLU"
        },

        { "type": "h2", "class": "text-xl lg:text-2xl text-medium mt-5 mb-3", "text": "Prasyarat" },
        {
            "type": "ul",
            "class": "list-disc pl-6 space-y-1",
            "items": [
                ".NET 7/8 SDK dan VS Code atau Visual Studio.",
                "Bot Framework Emulator untuk uji lokal.",
                "Ngrok (opsional) jika ingin menerima callback publik.",
                "Akun Azure (opsional) untuk publish dan channel."
            ]
        },

        { "type": "h2", "class": "text-xl lg:text-2xl text-medium mt-5 mb-3", "text": "Inisialisasi Proyek" },
        {
            "type": "pre",
            "class": "code-block language-bash",
            "text": """# Buat Web API minimal
dotnet new webapi -n DotNetBot
cd DotNetBot

# Tambah paket Bot Framework
dotnet add package Microsoft.Bot.Builder
dotnet add package Microsoft.Bot.Builder.Integration.AspNet.Core

# (Opsional) dialog, LUIS/recognizer
dotnet add package Microsoft.Bot.Builder.Dialogs
dotnet add package Microsoft.Bot.Builder.AI.Luis"""
        },

        { "type": "h2", "class": "text-xl lg:text-2xl text-medium mt-5 mb-3", "text": "Adapter HTTP" },
        {
            "type": "pre",
            "class": "code-block language-csharp",
            "text": """using Microsoft.Bot.Builder.Integration.AspNet.Core;
using Microsoft.Bot.Builder;
using Microsoft.Extensions.Logging;

public class AdapterWithErrorHandler : BotFrameworkHttpAdapter
{
    public AdapterWithErrorHandler(ILogger<BotFrameworkHttpAdapter> logger)
    {
        OnTurnError = async (turnContext, exception) =>
        {
            logger.LogError(exception, "Bot error");
            await turnContext.SendActivityAsync("Maaf, terjadi error. Coba lagi.");
        };
    }
}"""
        },

        { "type": "h2", "class": "text-xl lg:text-2xl text-medium mt-5 mb-3", "text": "Controller Endpoint" },
        {
            "type": "pre",
            "class": "code-block language-csharp",
            "text": """using Microsoft.AspNetCore.Mvc;
using Microsoft.Bot.Builder;
using Microsoft.Bot.Builder.Integration.AspNet.Core;

[ApiController]
[Route("api/messages")]
public class BotController : ControllerBase
{
    private readonly IBot _bot;
    private readonly BotFrameworkHttpAdapter _adapter;

    public BotController(BotFrameworkHttpAdapter adapter, IBot bot)
    {
        _adapter = adapter;
        _bot = bot;
    }

    [HttpPost, HttpGet]
    public async Task PostAsync()
        => await _adapter.ProcessAsync(Request, Response, _bot);
}"""
        },

        { "type": "h2", "class": "text-xl lg:text-2xl text-medium mt-5 mb-3", "text": "Bot Sederhana: Echo" },
        {
            "type": "pre",
            "class": "code-block language-csharp",
            "text": """using Microsoft.Bot.Builder;
using Microsoft.Bot.Schema;

public class EchoBot : ActivityHandler
{
    protected override async Task OnMessageActivityAsync(ITurnContext<IMessageActivity> context, CancellationToken ct)
    {
        var text = context.Activity.Text?.Trim();
        await context.SendActivityAsync(MessageFactory.Text($"Kamu berkata: {text}"), ct);
    }

    protected override async Task OnMembersAddedAsync(IList<ChannelAccount> membersAdded, ITurnContext<IConversationUpdateActivity> context, CancellationToken ct)
    {
        foreach (var m in membersAdded)
            if (m.Id != context.Activity.Recipient?.Id)
                await context.SendActivityAsync("Halo! Kirim pesan apa saja dan akan saya echo.", ct: ct);
    }
}"""
        },

        { "type": "h2", "class": "text-xl lg:text-2xl text-medium mt-5 mb-3", "text": "Registrasi Service (Program.cs)" },
        {
            "type": "pre",
            "class": "code-block language-csharp",
            "text": """var builder = WebApplication.CreateBuilder(args);

// Adapter + Bot
builder.Services.AddSingleton<BotFrameworkHttpAdapter, AdapterWithErrorHandler>();
builder.Services.AddSingleton<IBot, EchoBot>();

// State (in-memory untuk dev)
using Microsoft.Bot.Builder;
using Microsoft.Bot.Builder.MemoryStorage;
var storage = new MemoryStorage();
builder.Services.AddSingleton<IStorage>(storage);
builder.Services.AddSingleton<UserState>();
builder.Services.AddSingleton<ConversationState>();

var app = builder.Build();
app.MapControllers();
app.Run();"""
        },

        { "type": "h2", "class": "text-xl lg:text-2xl text-medium mt-5 mb-3", "text": "Menambah State di Bot" },
        {
            "type": "pre",
            "class": "code-block language-csharp",
            "text": """public class EchoBot : ActivityHandler
{
    private readonly UserState _userState;
    private readonly ConversationState _convState;
    private readonly IStatePropertyAccessor<string> _nameAccessor;

    public EchoBot(UserState userState, ConversationState convState)
    {
        _userState = userState;
        _convState = convState;
        _nameAccessor = _userState.CreateProperty<string>("name");
    }

    protected override async Task OnMessageActivityAsync(ITurnContext<IMessageActivity> context, CancellationToken ct)
    {
        var text = context.Activity.Text?.Trim().ToLowerInvariant();
        var name = await _nameAccessor.GetAsync(context, () => string.Empty, ct);

        if (text?.StartsWith("set nama ") == true)
        {
            name = text.Substring("set nama ".Length);
            await _nameAccessor.SetAsync(context, name, ct);
            await context.SendActivityAsync($"Nama disimpan: {name}", ct: ct);
        }
        else
        {
            await context.SendActivityAsync($"Hai {name or 'teman'} — kamu berkata: {context.Activity.Text}", ct: ct);
        }

        await _userState.SaveChangesAsync(context, false, ct);
        await _convState.SaveChangesAsync(context, false, ct);
    }
}"""
        },

        { "type": "h2", "class": "text-xl lg:text-2xl text-medium mt-5 mb-3", "text": "Dialog Waterfall (opsional)" },
        {
            "type": "pre",
            "class": "code-block language-csharp",
            "text": """using Microsoft.Bot.Builder.Dialogs;

public class ProfileDialog : ComponentDialog
{
    public ProfileDialog() : base(nameof(ProfileDialog))
    {
        var steps = new WaterfallStep[]
        {
            async (step, ct) => { return await step.PromptAsync("name", new PromptOptions{ Prompt = MessageFactory.Text("Siapa namamu?") }, ct); },
            async (step, ct) => { var name = (string)step.Result; await step.Context.SendActivityAsync($"Halo {name}!", ct: ct); return await step.EndDialogAsync(null, ct); }
        };
        AddDialog(new TextPrompt("name"));
        AddDialog(new WaterfallDialog(nameof(WaterfallDialog), steps));
        InitialDialogId = nameof(WaterfallDialog);
    }
}"""
        },

        { "type": "h2", "class": "text-xl lg:text-2xl text-medium mt-5 mb-3", "text": "Integrasi NLU (LUIS/CLU) singkat" },
        {
            "type": "pre",
            "class": "code-block language-csharp",
            "text": """// Pseudo: panggil recognizer lalu route intent
var (intent, score) = await RecognizeIntentAsync(context.Activity.Text);
if (intent == "Help") { await context.SendActivityAsync("Perintah: set nama <teks>, help, bye"); }
else if (intent == "Bye") { await context.SendActivityAsync("Sampai jumpa!"); }"""
        },

        { "type": "h2", "class": "text-xl lg:text-2xl text-medium mt-5 mb-3", "text": "Uji dengan Bot Framework Emulator" },
        {
            "type": "ul",
            "class": "list-disc pl-6 space-y-1",
            "items": [
                "Jalankan: dotnet run.",
                "Buka Emulator, Open Bot, endpoint: http://localhost:5000/api/messages (atau port proyekmu).",
                "Kirim pesan dan pastikan respon sesuai."
            ]
        },

        { "type": "h2", "class": "text-xl lg:text-2xl text-medium mt-5 mb-3", "text": "Deployment singkat" },
        {
            "type": "ul",
            "class": "list-disc pl-6 space-y-1",
            "items": [
                "Publish ke Azure App Service.",
                "Buat Azure Bot resource (Channel Registration) dan arahkan Messaging endpoint ke https://<app>/api/messages.",
                "Aktifkan channel (Teams, Telegram, Web Chat) sesuai kebutuhan."
            ]
        },

        { "type": "h2", "class": "text-xl lg:text-2xl text-medium mt-5 mb-3", "text": "Keamanan dan Praktik Baik" },
        {
            "type": "ul",
            "class": "list-disc pl-6 space-y-1",
            "items": [
                "Simpan secrets di Key Vault atau user-secrets, jangan di repo.",
                "Batasi ukuran payload dan rate limit endpoint.",
                "Aktifkan logging terstruktur dan correlation id.",
                "Gunakan penyimpanan state persisten (Cosmos/Blob) untuk produksi."
            ]
        },

        { "type": "h2", "class": "text-xl lg:text-2xl text-medium mt-5 mb-3", "text": "Troubleshooting umum" },
        {
            "type": "ul",
            "class": "list-disc pl-6 space-y-1",
            "items": [
                "401 pada Emulator: kosongkan MicrosoftAppId/MicrosoftAppPassword saat uji lokal.",
                "404: pastikan route api/messages benar dan controller terdaftar.",
                "Tidak ada balasan: cek OnTurnError dan log adapter, cek firewall/ngrok jika publik."
            ]
        },

        { "type": "h2", "class": "text-xl lg:text-2xl text-medium mt-5 mb-3", "text": "Kesimpulan" },
        {
            "type": "p",
            "class": "mb-2",
            "text": "Komponen inti bot di .NET: adapter untuk HTTP, controller sebagai endpoint, ActivityHandler untuk logika, state untuk konteks, dialog untuk alur, dan NLU untuk pemahaman. Mulai sederhana, amankan endpoint, lalu orkestrasi dialog dan channel sesuai kasus penggunaan."
        }
    ],
    "is_featured": True, 
    "tags": ["Bot Framework", ".NET", "C#", "NLU", "Dialog", "Azure"],
    "category": "Backend",
    "read_time": 10,
    "views": 0,
    "slug": "membangun-bot-dotnet-bot-framework-sdk"
}
