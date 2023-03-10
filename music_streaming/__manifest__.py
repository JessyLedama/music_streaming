{
    'name': 'Music Streaming',
    'version': '1.0',
    'category': 'Website',
    'author': 'SIMI Technologies',
    'summary': 'Allow users to upload and stream music on the website',
    'description': """
    
    This module allows authenticated users to upload music, either as singles or part of an album, and create playlists of their favorite songs. Uploaded songs are available for streaming on the website.
    
    The module utilizes python-magic for file identification. install python-magic using pip before installing this module.
    """,
    'depends': [
        'base',
        'web',
        'website',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/songs.xml',
        # 'views/assets.xml',
        # 'views/song_views.xml',
        # 'views/album_views.xml',
        # 'views/playlist_views.xml',
        # 'views/website_templates.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'auto_install': False,
}
