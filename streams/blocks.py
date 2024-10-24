from wagtail import blocks

class EmbedVideoBlock(blocks.StructBlock):
    video_url = blocks.URLBlock(required=True, help_text="Add youtube video URL")

    class Meta:  #noqa
        template = "streams/embed_video_block.html"
        icon = "media"
        label = "Embed Video"