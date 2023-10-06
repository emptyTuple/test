import os
from contextlib import contextmanager
from tempfile import NamedTemporaryFile


@contextmanager
def safe_write(filename):
    tmp = NamedTemporaryFile("w", encoding="utf-8", delete=False)
    try:
        yield tmp
    except Exception as e:
        tmp.close()
        os.unlink(tmp.name)

        print(
            f"Во время записи в файл было возбуждено исключение {e.__class__.__name__}"
        )
    else:
        try:
            tmp.close()
            os.replace(tmp.name, filename)
        except Exception as e:
            os.unlink(tmp.name)
            print(
                f"Во время записи в файл было возбуждено исключение {e.__class__.__name__}"
            )


with safe_write("under_tale.txt") as file:
    file.write("Тень от руин нависает над вами, наполняя вас решительностью\n")

with safe_write("under_tale.txt") as file:
    print("Под весёлый шорох листвы вы наполняетесь решительностью", file=file)
    raise ValueError

with open("under_tale.txt") as file:
    print(file.read())
