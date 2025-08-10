from app.models.user import User
from app.models.tasks import Task
from app.models.expenses import Expense
from app.core.database import engine, Base

# Registrar modelos
Base.metadata.create_all(bind=engine)