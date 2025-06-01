import os
from dotenv import load_dotenv
load_dotenv()

print("loading the env variables")

# POSTGRES_USER = os.getenv("POSTGRES_USER")
# POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
# POSTGRES_DB = os.getenv("POSTGRES_DB")
# POSTGRES_HOST = os.getenv("POSTGRES_HOST")
# POSTGRES_PORT = os.getenv("POSTGRES_PORT")

DATABASE_URL = "postgresql://postgres:ChXRdHnBewpbIdErnPFXZBuKzruvRyBs@shortline.proxy.rlwy.net:50850/railway"

# DATABASE_URL = "postgresql://postgres:CHERRYCHARAN2380@db.fnzlghlygtunsbiiihyp.supabase.co:5432/postgres"
