from sqlalchemy import create_engine, text

engine =create_engine("mysql://ptarsoneves:Strolandia1@database-1.cizel514jz3i.us-east-2.rds.amazonaws.com/carreira-python")

def carrega_vagas_db():
  with engine.connect() as conn:
      resultado = conn.execute(text("SELECT * FROM vagas"))
      vagas = []
      for vaga in resultado.all():
          vagas.append(vaga._asdict())
      return vagas