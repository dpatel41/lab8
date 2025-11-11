from adventure.utils import read_events_from_file
from rich.console import Console
from rich.prompt import Prompt
import random

console = Console()


def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "You stand still, unsure what to do. The forest swallows you."


def left_path(event):
    return "You walk left. " + event


def right_path(event):
    return "You walk right. " + event


def main():
    events = read_events_from_file("events.txt")

    console.print(
        "[bold magenta]You wake up in a dark forest.[/bold magenta] "
        "[cyan]You can go [bold green]left[/bold green] or "
        "[bold yellow]right[/bold yellow].[/cyan]"
    )

    while True:
        choice = Prompt.ask(
            "[bold cyan]Which direction do you choose?[/bold cyan] "
            "[green](left)[/green]/[yellow](right)[/yellow]/[red](exit)[/red]"
        )
        choice = choice.strip().lower()

        if choice == "exit":
            console.print(
                "[bold red]You decide to leave the forest. "
                "The adventure ends here.[/bold red]"
            )
            break

        result = step(choice, events)

        if choice == "left":
            console.print(f"[green]{result}[/green]")
        elif choice == "right":
            console.print(f"[yellow]{result}[/yellow]")
        else:
            console.print(f"[dim]{result}[/dim]")


if __name__ == "__main__":
    main()
