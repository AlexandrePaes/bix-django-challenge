.PHONY: build
build:
	docker-compose run --rm web sh -c "python manage.py collectstatic"
.PHONY: deploy
deploy: 
	docker-compose -f docker-compose-deploy.yml run --rm --remove-orphans gcloud sh -c "gcloud app deploy --project bixdjangohotel"