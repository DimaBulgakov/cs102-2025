"""Модуль для работы с текстовыми сообщениями"""

def get_message(name: str = "World") -> str:
    """
    Генерирует приветственное сообщение.

    Args:
        name: Имя для приветствия.

    Returns:
        Строка приветствия.
    """
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(get_message())
