import persistence
import threading
import interface as ui
from rich.live import Live
import requests
import time
from rich.table import Table

stop_flag = False
url_path = "site_urls.json"
email_path = "emails.json"

def add_url():
    ui.add_url_text()
    url = input()
    urls = persistence.load(url_path)
    if url in urls:
        ui.duplicated_url_error()
    else:
        persistence.add_content(url,url_path)
        ui.success_url_added()
    close_function()

def close_function():
    ui.close_function_message()
    return input()

def list_sites():
    urls = persistence.load(url_path)
    ui.list_monitored_sites(urls)
    close_function()

def check_sites():
    global stop_flag
    stop_flag = False
    sites = persistence.load(url_path)

    thread = threading.Thread(target=wait_for_enter)
    thread.start()

    with Live(build_table(sites), refresh_per_second=1) as live:
        while not stop_flag:
            time.sleep(1)
            live.update(build_table(sites))

def build_table(sites):
        table = Table(title="Site Monitor")
        table.add_column("Site", style="cyan", no_wrap=True)
        table.add_column("Status", style="magenta")
        table.add_column("Message", style="green")

        for site in sites:
            status = check_url(site)
            status_text = "[green]Online[/green]" if status else "[red]Offline[/red]"
            msg = "Ok" if status else "[red]Failed to Connect[/red]"
            table.add_row(site, status_text, msg)
        
        return table

def check_url(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

def wait_for_enter():
    global stop_flag
    close_function()
    stop_flag = True

def delete_url():
    confirm_delete = False
    urls = persistence.load(url_path)

    if not urls:
        ui.none_urls_to_remove()
        return

    while not confirm_delete:
        title = "[bold red]Delete URL[/bold red]"
        options = urls + ["[italic]Exit to main menu[/italic]"]
        menu_options = list(range(1, len(options) + 1))
        border_style = "bright_red"
        numbers_color= "bright_red"

        ui.show_interactive_menu(0, options, title,border_style,numbers_color)
        option = ui.read_option(menu_options)

        if option == len(options):
            ui.cancell_message()
            break

        ui.show_interactive_menu(option, options, title, border_style, numbers_color)
        ui.confirm_menu() 
        delete = ui.read_option([1, 2])

        if delete == 1:
            url_removida = urls.pop(option - 1)
            persistence.save(urls,url_path)
            ui.deletion_confirmed_message(url_removida)
            confirm_delete = True
        else:
            ui.cancell_message()
    close_function()

def add_email():
    emails = persistence.load(email_path)
    email = input()

    if not(email in emails):
        persistence.add_content(email,email_path)
    else:
        ui.email_duplicated_error()

    close_function()


