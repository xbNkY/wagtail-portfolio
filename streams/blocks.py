from wagtail import blocks


class TitleAndTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.TextBlock(required=True, help_text="Add additional text")

    class Meta:  #noqa
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"


class EmbedVideoBlock(blocks.StructBlock):
    video_url = blocks.URLBlock(required=True, help_text="Add youtube video URL")

    class Meta:  #noqa
        template = "streams/embed_video_block.html"
        icon = "media"
        label = "Embed Video"