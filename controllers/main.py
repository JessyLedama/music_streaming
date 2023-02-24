# music_streaming/controllers/main.py

from odoo import http
from odoo.http import request

class MusicStreamingController(http.Controller):
    
    @http.route('/music_streaming', auth='user', website=True)
    def music_streaming(self, **kwargs):
        songs = request.env['music.song'].search([])
        return request.render('music_streaming.songs', {'songs': songs})

    @http.route('/music_streaming/song/<int:song_id>', auth='user', website=True)
    def music_streaming_song(self, song_id, **kwargs):
        song = request.env['music.song'].sudo().browse(song_id)
        return request.render('music_streaming.song', {'song': song})
