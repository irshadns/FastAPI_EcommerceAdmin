build:
	pip install -r requirements.txt
	python -m app.pre-run-backend.db_init
	alembic revision --autogenerate -m "initial"
	alembic upgrade head
	python -m app.pre-run-backend.create_admin_user
	python -m app.pre-run-backend.ingest_ecommerce_data

migrate:
	alembic upgrade head

runserver:
	bash -c "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"