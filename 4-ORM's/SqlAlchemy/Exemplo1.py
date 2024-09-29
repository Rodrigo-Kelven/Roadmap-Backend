from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuração da base
Base = declarative_base()
engine = create_engine('sqlite:///tasks.db')
Session = sessionmaker(bind=engine)
session = Session()

# Modelo de dados
class Task(Base):
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String, nullable=True)
    completed = Column(Integer, default=0)  # 0 = False, 1 = True

# Criar as tabelas
Base.metadata.create_all(engine)

# Funções CRUD
def create_task(title, description):
    task = Task(title=title, description=description)
    session.add(task)
    session.commit()
    return task

def get_tasks():
    return session.query(Task).all()

# Exemplo de uso
if __name__ == "__main__":
    create_task("Estudar SQLAlchemy", "Ler a documentação")
    tasks = get_tasks()
    for task in tasks:
        print(f"ID: {task.id}, Title: {task.title}, Completed: {task.completed}")
