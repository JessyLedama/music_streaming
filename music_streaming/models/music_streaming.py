# music_streaming/models/music_streaming.py

import magic
from odoo import models, fields, api

class MusicSong(models.Model):
    _name = 'music.song'
    _description = 'Music Song'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(string="Title", required=True)
    artist = fields.Char(string="Artist", required=True)
    album = fields.Many2one('music.album', string="Album")
    cover = fields.Binary(string="Cover")
    file = fields.Binary(string="File", required=True)
    filename = fields.Char(string="File Name", required=True)
    mime_type = fields.Char(string="MIME Type", compute='_compute_mime_type')
    duration = fields.Float(string="Duration", compute='_compute_duration')
    user_id = fields.Many2one('res.users', string="User", default=lambda self: self.env.user)

    @api.depends('file')
    def _compute_mime_type(self):
        for record in self:
            record.mime_type = magic.from_buffer(record.file, mime=True)
    
    @api.depends('file')
    def _compute_duration(self):
        for record in self:
            with tempfile.NamedTemporaryFile(delete=True) as f:
                f.write(base64.b64decode(record.file))
                f.flush()
                with audioread.audio_open(f.name) as audio:
                    record.duration = audio.duration
    
class MusicAlbum(models.Model):
    _name = 'music.album'
    _description = 'Music Album'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", required=True)
    artist = fields.Char(string="Artist", required=True)
    cover = fields.Binary(string="Cover")
    songs = fields.One2many('music.song', 'album', string="Songs")



