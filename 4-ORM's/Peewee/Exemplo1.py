from peewee import SqliteDatabase, Model, IntegerField, CharField, BooleanField

# Configuração da base
db = SqliteDatabase('tasks.db')

# Modelo de dados
class Task(Model):
    title = CharField()
    description = CharField(null=True)
    completed = BooleanField(default=False)

    class Meta:
        database = db

# Criar as tabelas
db.connect()
db.create_tables([Task])

# Funções CRUD
def create_task(title, description):
    task = Task.create(title=title, description=description)
    return task

def get_tasks():
    return Task.select()

# Exemplo de uso
if __name__ == "__main__":
    create_task("Estudar Peewee", "Ler a documentação")
    tasks = get_tasks()
    for task in tasks:
        print(f"ID: {task.id}, Title: {task.title}, Completed: {task.completed}")
