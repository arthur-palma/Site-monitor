from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress
from rich.progress import Progress, BarColumn, TextColumn
import time

console = Console()

def welcome_message():
    console.print("\n[bold cyan]Welcome to Sites Monitor![/bold cyan]")
    console.print("[green]Your tool for real-time website status checking.[/green]\n")

def loading_bar():
    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=20, complete_style="white", finished_style="white", pulse_style="white"),
        TextColumn("{task.completed}/{task.total}")
    ) as progress:
        task = progress.add_task("Loading application...", total=100)
        for _ in range(100):
            time.sleep(3 / 100)
            progress.update(task, advance=1)

def read_option(valid_options):
    while True:
        try:
            option = int(console.input("\n[bold white]Select an option: [/bold white] "))
            if option in valid_options:
                return option
            else:
                console.print("[red]Select a valid option![/red]")
        except ValueError:
            console.print("[red]Only numbers accepted[/red]")

def show_interactive_menu(selected_option,options,title,border_color,numbers_color):
    menu_text = ""
    for i, option in enumerate(options, start=1):
        if i == selected_option:
            menu_text += f"[bold green]> {i}. {option}[/bold green]\n"
        else:
            menu_text += f"[bold {numbers_color}]  {i}.[/bold {numbers_color}] {option}\n"

    panel = Panel.fit(menu_text.strip(), title=title, border_style=border_color)
    console.clear()
    console.print(panel)

def main_menu():
    while True:
        menu_options = [1,2,3,4,5,6]
        title = "[bold cyan]Sites monitor[/bold cyan]"
        options = [
        "Add URL for monitoring",
        "List monitored sites",
        "Check website status",
        "Remove URL",
        "Add E-mail",
        "Exit"
        ]
        border_style = "bright_blue"
        number_colors = "blue"
        show_interactive_menu(0,options,title,border_style,number_colors)
        option = read_option(menu_options)
        show_interactive_menu(option,options,title,border_style,number_colors)
        return option

def add_url_text():
    console.print("[bold white]Please enter the URL you want to add:[/bold white]")

def success_url_added():
    console.print("[bold white]URL successfully added.[/bold white]")

def close_function_message():
    console.print("[bold yellow]Press Enter to return to menu[/bold yellow]")

def list_monitored_sites(urls):
    table = Table(title="Monitored sites")
    table.add_column("Site", style="cyan", no_wrap=True)
    for url in urls:
        table.add_row(url)
    console.print(table)

def duplicated_url_error():
    console.print("[bold red]This URL is already under monitoring.[/bold red]")

def cancell_message():
    console.print("[bold yellow]Cancelling.[/bold yellow]")

def deletion_confirmed_message(url_removida):
    console.print(f"[bold green]URL {url_removida} removed successfully.[/bold green]")

def none_urls_to_remove():
    console.print("[bold red]None URLS to remove.[/bold red]")

def confirm_menu():
    panel = Panel.fit(
        "[bold green]1 - YES[/bold green]\n"
        "[bold red]2 - NO[/bold red]",
        title="[bold]Confirm Deletion?[/bold]",
        border_style="bold white"
    )
    console.print(panel)

def exit_message():
    console.print("\n\n[bold green]Thanks for using Sites Monitor![/bold green]")
    console.print("Goodbye and have a great day! 👋\n\n")

def email_duplicated_error():
    console.print("[bold red]This email is already registred.[/bold red]")

def add_email_text():
    console.print("[bold white]Please enter the email you want to add to receive notifications:[/bold white]")

def invalid_email_error():
    console.print("[bold red]This is not a valid email.[/bold red]")