"""Open all extracted images grouped by slide so we can identify them visually."""
import os, subprocess

img_dir = 'images'
# Key slides and their images
slide_map = {
    'Slide1_Cover':        ['image3.jpg', 'image2.png'],
    'Slide2_Issue':        ['image4.png', 'image6.jpg', 'image5.jpg'],
    'Slide3_Problem':      ['image7.jpg'],
    'Slide4_List':         ['image9.jpg', 'image8.png'],
    'Slide5_CaseStudy':    ['image10.jpg'],
    'Slide6_Architecture': ['image17.jpg','image12.png','image16.jpg','image11.png',
                            'image15.jpg','image20.jpg','image14.jpg','image19.jpg',
                            'image13.png','image18.jpg'],
    'Slide7_Snapshots':    ['image22.jpg','image21.jpg','image25.jpg','image24.jpg','image23.jpg'],
    'Slide8_Technology':   ['image27.png','image26.png'],
    'Slide9_Market':       ['image29.png','image28.png','image31.png','image30.png'],
}

for slide, imgs in slide_map.items():
    print(f'\n{slide}:')
    for img in imgs:
        path = os.path.join(img_dir, img)
        size = os.path.getsize(path) if os.path.exists(path) else 0
        print(f'  {img} ({size:,} bytes)')
