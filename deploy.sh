# if [ "${CIRCLE_BRANCH}" == "master" ]; then
# 	echo "Mandndo a heroku"
# 	heroku container:push web --app $HEROKU_APP_NAME
# 	echo "Se mando a heroku"
# 	# git push --force git@heroku.com:$HEROKU_APP_NAME.git HEAD:refs/heads/master
# 	# heroku run python manage.py deploy
# 	# heroku restart
# fi

echo "Mandndo a heroku"
sudo heroku container:login
sudo heroku container:push web --app $HEROKU_APP_NAME
echo "Se mando a heroku"