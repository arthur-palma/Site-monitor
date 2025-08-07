import interface as ui
import monitor

def main():
    ui.welcome_message()
    ui.loading_bar()
    while True:
        option = ui.main_menu()

        match option:
            case 1:
                monitor.add_url()
            case 2:
                monitor.list_sites()
            case 3:
                monitor.check_sites()
            case 4:
                monitor.delete_url()
            case _:
                ui.exit_message()
                break

if __name__ == "__main__":
    main()