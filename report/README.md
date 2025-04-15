# Звіт до роботи: Автоматизація тестування за допомогою GitHub Actions

## Мета роботи

Ознайомитися з принципами автоматизації тестування програм за допомогою CI/CD-системи GitHub Actions. Навчитись створювати Workflows, налаштовувати тригери запуску, працювати з декількома задачами (jobs) та умовами їх виконання.

---

## Хід виконання

### Крок 1. Створення репозиторію

У GitHub було створено репозиторій `actions`, до якого додано наступні файли:

- `app.py` — головний файл із класом `Figure`;
- `test_app.py` — модуль з тестом для функції `get_angles`;
- `.github/workflows/python-app.yml` — конфігураційний файл GitHub Actions;
- `README.md` — документ з описом проєкту і бейджем для відображення статусу.

---

### Крок 2. Основний код

**app.py**
```python
class Figure:
    def __init__(self, type, length) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in ["квадрат", "прямокутник", "трикутник"], "Дозволені фігури: квадрат, прямокутник, трикутник"
        self.type = type
        self.length = length

    def get_angles(self):
        if self.type == "трикутник":
            return 3
        return 4
```

**test_app.py**
```python
from app import Figure

def test_get_angles():
    fig = "трикутник"
    triangle = Figure(fig, 1)
    assert triangle.get_angles() == 3, f"У {fig} має бути 3 кути!"
```

---

### Крок 3. Створення Workflow

**.github/workflows/python-app.yml**
```yaml
name: Python application

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]
  workflow_dispatch:  # ручний запуск

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pytest

    - name: Run tests
      run: |
        pytest
```

---

### Крок 4. Запуск за розкладом
```yaml
on:
  schedule:
    - cron: '30 12 * * 1'  # кожного понеділка о 12:30
```

---

### Крок 5. Створення другого Workflow

**.github/workflows/manual-workflow.yml**
```yaml
name: Manual Workflow

on:
  workflow_dispatch:
    inputs:
      name:
        description: 'Enter your name'
        required: true
        default: 'Executer'

jobs:
  greet:
    runs-on: ubuntu-latest
    steps:
      - name: Send greeting
        run: echo "Hello ${{ github.event.inputs.name }}"
        if: github.event.inputs.name != 'Executer'
```

---

### Крок 6. Декілька Jobs
```yaml
jobs:
  one:
    name: First Job
    runs-on: ubuntu-latest
    steps:
      - name: Echo first
        run: echo "This is the first job"

  two:
    name: Second Job
    runs-on: ubuntu-latest
    steps:
      - name: Echo second
        run: echo "This is the second job"
```

---

### Крок 7. Бейдж у README.md

У файл `README.md` додано Markdown-бейдж:
```markdown
![Python application](https://github.com/Kaena0/actions/actions/workflows/python-app.yml/badge.svg)
```

---

## Висновки

У ході виконання роботи було:

- створено репозиторій та основні скрипти;
- реалізовано автоматичне тестування коду через GitHub Actions;
- налаштовано ручний запуск та запуск за розкладом;
- створено кілька jobs і workflows;
- додано бейдж зі статусом виконання.

Цей підхід дозволяє зробити процес тестування стабільним, повторюваним і прозорим, що є важливою частиною сучасної розробки програмного забезпечення.
