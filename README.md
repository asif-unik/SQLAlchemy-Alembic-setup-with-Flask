Step to setup alembic:-

    1.>pip install alembic
    2.>alembic init alembic
    3.Open 'alembic.ini' file update sqlalchemy.url by your database
    4.To create alembic version:
        >alembic revision -m "create table"
    5.To upgrate alembic version as latest or specific version
        >alembic upgrade head (for latest alembic version)
        >alembic upgrade <alembic version>
    6.To downgrade alembic version
        >alembic downgrade -1 (for downgrade to previous alembic version)
        >alembic downgrade <alembic version>
    7. To check current alembic version
        >alembic current
    8.To check History
        >alembic history
        
