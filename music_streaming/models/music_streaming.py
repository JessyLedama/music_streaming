# music_streaming/models/music_streaming.py

import magic
from odoo import api, fields, models


class MusicStreaming(models.Model):
    _name = 'music.streaming'
    _description = 'Music Streaming'

    name = fields.Char(required=True)
    file = fields.Binary(required=True)
    mime_type = fields.Char()

    @api.model
    def create(self, vals):
        record = super(MusicStreaming, self).create(vals)
        record.mime_type = magic.from_buffer(record.file, mime=True)
        return record


class MusicStreamingMenu(models.Model):
    _name = 'music.streaming.menu'
    _description = 'Music Streaming Menu'

    def _get_default_view_id(self):
        return self.env.ref('music_streaming.music_streaming_tree_view').id

    name = fields.Char(required=True)
    view_id = fields.Many2one('ir.ui.view', default=_get_default_view_id)
    
    @api.model
    def _update_menuitems(self):
        action = self.env.ref('music_streaming.music_streaming_form_view')
        menuitem = self.env.ref('music_streaming.music_streaming_menuitem')
        menuitem.write({'action': action.id})


class MusicStreamingController(models.AbstractModel):
    _name = 'music.streaming.controller'
    _inherit = 'website.multi.mixin'

    def list(self, **kwargs):
        songs = self.env['music.streaming'].search([])
        return self._show_list(songs)

    def _show_list(self, songs):
        return self._response('music_streaming.listing', {'songs': songs})


class MusicStreamingWebsite(models.Model):
    _inherit = 'website'

    @http.route('/music_streaming', type='http', auth="public", website=True)
    def music_streaming(self, **kwargs):
        return self._call_controller('music.streaming.controller', 'list', **kwargs)

