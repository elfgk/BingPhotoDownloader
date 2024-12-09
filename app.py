import gradio as gr
from bing_image_downloader import downloader

def downloader_images(search_query, limit, adult_filter_off, timeout=20):
    # Bing'den resim indirme işlemi
    adult_filter = adult_filter_off == "True"
    downloader.download(
        search_query,
        limit=limit,
        adult_filter_off=adult_filter,
        force_replace=False,
        timeout=timeout
    )
    return f'{limit} adet "{search_query}" fotoğrafı indirildi.'

# Gradio arayüzü oluştur
interface = gr.Interface(
    fn=downloader_images,
    inputs=[
        gr.Textbox(label='Aranacak kelime'),
        gr.Slider(1, 100, step=5, label='Görsel sayısı'),
        gr.Radio(["True", "False"], label="Korumalı mod", value="True")
    ],
    outputs="text",
    title="Bing ile görsel indirme",
    description="İndirmek istediğiniz resmi tanımlayınız. İlgili ayarlardan korumalı mod seçeneğini ve indirmek istediğiniz görsel sayısını belirleyebilirsiniz.",
    examples=[
        ["cat", 20, "True"]
    ]
)

# Arayüzü başlat
interface.launch(share=True)