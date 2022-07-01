#settings.py

INSTALLED_APPS=[
	'My_app_name'
]

templates = {
	dirs:[os.path.join(BASE_DIR, 'templates/')]
}

STATIC.FILES_DIR=[os.path.join(BASE_DIR, 'Static/')]

