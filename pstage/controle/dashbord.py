from grappelli.dashboard import modules, Dashboard


class CustomIndexDashboard(Dashboard):
    def init_with_context(self, context):
        # Titre de la page d'accueil
        self.children.append(modules.Group(
            title="Tableau de Bord",
            column=1,
            collapsible=True,
            children=[
                modules.AppList(
                    title="Applications",
                    column=1,
                    collapsible=True,
                    models=('auth.*', 'controle*'),  # Remplacez 'myapp' par le nom de votre application
                ),
                modules.LinkList(
                    title="Liens Rapides",
                    column=1,
                    children=[
                        {
                            'title': 'Site Web',
                            'url': 'https://www.example.com',
                            'external': True,
                        },
                        {
                            'title': 'Documentation',
                            'url': 'https://docs.example.com',
                            'external': True,
                        },
                    ],
                ),
                modules.RecentActions(
                    title="Actions Récentes",
                    column=2,
                    collapsible=False,
                    limit=5,
                ),
            ]
        ))