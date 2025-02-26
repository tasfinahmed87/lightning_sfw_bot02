# ruff: noqa: RUF012
from bot.core.config_manager import Config

i = Config.CMD_SUFFIX


class BotCommands:
    StartCommand = "start2"
    MirrorCommand = [f"mirror2{i}", f"m2{i}"]
    JdMirrorCommand = [f"jdmirror2{i}", f"jm2{i}"]
    NzbMirrorCommand = [f"nzbmirror2{i}", f"nm2{i}"]
    YtdlCommand = [f"ytdl2{i}", f"y2{i}"]
    LeechCommand = [f"leech2{i}", f"l2{i}"]
    JdLeechCommand = [f"jdleech2{i}", f"jl2{i}"]
    NzbLeechCommand = [f"nzbleech2{i}", f"nl2{i}"]
    YtdlLeechCommand = [f"ytdlleech2{i}", f"yl2{i}"]
    CloneCommand = f"clone2{i}"
    MediaInfoCommand = f"mediainfo2{i}"
    CountCommand = f"count2{i}"
    DeleteCommand = f"del2{i}"
    CancelAllCommand = f"cancelall2{i}"
    ForceStartCommand = [f"forcestart2{i}", f"fs2{i}"]
    ListCommand = f"list2{i}"
    SearchCommand = f"search2{i}"
    HydraSearchCommamd = f"nzbsearch2{i}"
    StatusCommand = f"status2{i}"
    UsersCommand = f"users2{i}"
    AuthorizeCommand = f"auth2{i}"
    UnAuthorizeCommand = f"unauth2{i}"
    AddSudoCommand = f"addsudo2{i}"
    RmSudoCommand = f"rmsudo2{i}"
    PingCommand = f"ping2{i}"
    RestartCommand = f"restart2{i}"
    RestartSessionsCommand = f"restartses2{i}"
    StatsCommand = f"stats2{i}"
    HelpCommand = f"help2{i}"
    LogCommand = f"log2{i}"
    ShellCommand = f"shell2{i}"
    AExecCommand = f"aexec2{i}"
    ExecCommand = f"exec2{i}"
    ClearLocalsCommand = f"clearlocals2{i}"
    BotSetCommand = f"botsettings2{i}"
    UserSetCommand = f"settings2{i}"
    SpeedTest = f"speedtest2{i}"
    BroadcastCommand = [f"broadcast2{i}", "broadcastall"]
    SelectCommand = f"sel2{i}"
    RssCommand = f"rss2{i}"
