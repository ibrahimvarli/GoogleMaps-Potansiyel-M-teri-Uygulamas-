import sqlite3
import json
from datetime import datetime
from pathlib import Path

class Database:
    def __init__(self):
        db_path = Path("data/business_data.db")
        db_path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(db_path)
        self.create_tables()
    
    def create_tables(self):
        cursor = self.conn.cursor()
        
        # İşletmeler tablosu
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS businesses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            place_id TEXT UNIQUE,
            name TEXT,
            address TEXT,
            phone TEXT,
            category TEXT,
            rating FLOAT,
            lat FLOAT,
            lng FLOAT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        # Müşteriler tablosu
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE,
            phone TEXT,
            address TEXT,
            preferences TEXT,
            last_visit DATE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        # Ziyaretler tablosu
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS visits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            business_id INTEGER,
            visit_date DATE,
            notes TEXT,
            FOREIGN KEY (customer_id) REFERENCES customers (id),
            FOREIGN KEY (business_id) REFERENCES businesses (id)
        )
        ''')
        
        # Üyelik tablosu
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS subscriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            plan_type TEXT CHECK(plan_type IN ('free', 'pro')),
            start_date DATE,
            end_date DATE,
            payment_status TEXT,
            amount FLOAT,
            FOREIGN KEY (user_id) REFERENCES customers (id)
        )
        ''')
        
        # Kullanıcılar tablosu
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            email TEXT UNIQUE,
            plan_type TEXT DEFAULT 'free',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        self.conn.commit()

    # Database metodları buraya... 