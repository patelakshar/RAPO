from __future__ import annotations

from typing import Any

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console = Console()


def _format_value(value: Any) -> str:
    if value is None:
        return "N/A"

    if isinstance(value, bool):
        return "✅ Yes" if value else "❌ No"

    if isinstance(value, dict):
        if not value:
            return "N/A"
        return "\n".join(f"{k}: {_format_value(v)}" for k, v in value.items())

    if isinstance(value, (list, tuple, set)):
        if not value:
            return "N/A"
        return "\n".join(str(item) for item in value)

    return str(value)


def _render_section(title: str, data: Any) -> None:
    table = Table(show_header=False, box=None, pad_edge=False)

    table.add_column("Field", style="bold cyan", width=28)
    table.add_column("Value", overflow="fold")

    if isinstance(data, dict):
        if data:
            for key, value in data.items():
                table.add_row(str(key), _format_value(value))
        else:
            table.add_row("Value", "N/A")
    else:
        table.add_row("Value", _format_value(data))

    console.print(
        Panel(
            table,
            title=f"[bold cyan]{title}[/bold cyan]",
            border_style="bright_blue",
            expand=True,
        )
    )


def _render_robots_section(robots_data: Any) -> None:
    if not isinstance(robots_data, dict) or not robots_data.get("exists", False):
        console.print(
            Panel(
                "[bold yellow]Not Found[/bold yellow]",
                title="[bold cyan]🤖 Robots.txt[/bold cyan]",
                border_style="bright_blue",
                expand=True,
            )
        )
        return

    table = Table(show_header=False, box=None, pad_edge=False)
    table.add_column("Field", style="bold cyan", width=28)
    table.add_column("Value", overflow="fold")

    table.add_row("Exists", "Yes")
    table.add_row("Status", str(robots_data.get("status", 0)))
    table.add_row("User Agents", _format_value(robots_data.get("user_agents", [])))
    table.add_row("Allow Rules", _format_value(robots_data.get("allow", [])))
    table.add_row("Disallow Rules", _format_value(robots_data.get("disallow", [])))
    table.add_row("Sitemaps", _format_value(robots_data.get("sitemaps", [])))

    console.print(
        Panel(
            table,
            title="[bold cyan]🤖 Robots.txt[/bold cyan]",
            border_style="bright_blue",
            expand=True,
        )
    )


def _render_sitemap_section(sitemap_data: Any) -> None:
    if not isinstance(sitemap_data, dict) or not sitemap_data.get("exists", False):
        console.print(
            Panel(
                "[bold yellow]Not Found[/bold yellow]",
                title="[bold cyan]📄 Sitemap[/bold cyan]",
                border_style="bright_blue",
                expand=True,
            )
        )
        return

    urls = sitemap_data.get("urls", []) or []
    preview = urls[:10]
    value = "\n".join(preview) if preview else "N/A"

    table = Table(show_header=False, box=None, pad_edge=False)
    table.add_column("Field", style="bold cyan", width=28)
    table.add_column("Value", overflow="fold")

    table.add_row("Exists", "Yes")
    table.add_row("Status", str(sitemap_data.get("status", 0)))
    table.add_row("Number of URLs", str(len(urls)))
    table.add_row("URLs", value)

    console.print(
        Panel(
            table,
            title="[bold cyan]📄 Sitemap[/bold cyan]",
            border_style="bright_blue",
            expand=True,
        )
    )


def _get_section(results: dict[str, Any], *keys: str) -> Any:
    for key in keys:
        if key in results:
            return results[key]
    return None


def display(results: dict[str, Any]) -> None:
    """Display RAPO scan results."""

    logo = Text(
        """\
██████╗  █████╗ ██████╗  ██████╗
██╔══██╗██╔══██╗██╔══██╗██╔═══██╗
██████╔╝███████║██████╔╝██║   ██║
██╔══██╗██╔══██║██╔═══╝ ██║   ██║
██║  ██║██║  ██║██║     ╚██████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝      ╚═════╝

Red-team Automated Pen-testing Operator
Version 0.1
""",
        style="bold cyan",
        justify="center",
    )

    console.print()

    console.print(
        Panel(
            logo,
            border_style="bright_blue",
            expand=False,
        )
    )

    console.print()

    _render_section("🎯 Target", _get_section(results, "target", "target_info"))
    _render_section("🌐 DNS", _get_section(results, "dns", "dns_results"))
    _render_section("🌍 HTTP", _get_section(results, "http", "http_results"))
    _render_section("🔓 Open Ports", _get_section(results, "ports", "open_ports", "ports_results"))
    _render_section("📄 WHOIS", _get_section(results, "whois", "whois_results"))
    _render_section("🛠 Technologies", _get_section(results, "technologies", "tech", "tech_results"))
    _render_section("🔒 SSL", _get_section(results, "ssl", "ssl_results"))
    _render_section("🛡 Security Headers", _get_section(results, "security_headers", "headers", "headers_results"))
    _render_robots_section(_get_section(results, "robots"))
    _render_sitemap_section(_get_section(results, "sitemap"))

    console.print(
        Panel(
            "[bold green]✔ Scan Complete[/bold green]",
            border_style="green",
            expand=False,
        )
    )