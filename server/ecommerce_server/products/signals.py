
import json
import os
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Product, Supplier, Category
import requests
from django.core.files.base import ContentFile

@receiver(post_migrate)
def populate_data(sender, **kwargs):
    # Path to your sample JSON file
    json_file_path = os.path.join(os.path.dirname(__file__), 'sample_data', 'products.json')

    # Load data from JSON file
    sample_products = [
        {
        "name": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
        "description": "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday",
        "price": 109.95,
        "brand": "Fjallraven",
        "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg",
        "stock": 120,
        "rating": {
            "rate": 3.9,
            "count": 120
        },
        "created_at": "2025-01-21",
        "updated_at": "2025-01-21",
        "supplier": "Fjallraven",
        "category": "men's clothing"
    },
    {
        "name": "Mens Casual Premium Slim Fit T-Shirts",
        "description": "Slim-fitting style, contrast raglan long sleeve, three-button henley placket, light weight & soft fabric for breathable and comfortable wearing. And Solid stitched shirts with round neck made for durability and a great fit for casual fashion wear and diehard baseball fans. The Henley style round neckline includes a three-button placket.",
        "price": 22.3,
        "brand": "Casual",
        "image": "https://fakestoreapi.com/img/71-3HjGNDUL._AC_SY879._SX._UX._SY._UY_.jpg",
        "stock": 259,
        "rating": {
            "rate": 4.1,
            "count": 259
        },
        "created_at": "2025-01-21",
        "updated_at": "2025-01-21",
        "supplier": "Casual",
        "category": "men's clothing"
    },
    {
        "name": "Mens Cotton Jacket",
        "description": "great outerwear jackets for Spring/Autumn/Winter, suitable for many occasions, such as working, hiking, camping, mountain/rock climbing, cycling, traveling or other outdoors. Good gift choice for you or your family member. A warm hearted love to Father, husband or son in this thanksgiving or Christmas Day.",
        "price": 55.99,
        "brand": "Menswear",
        "image": "https://fakestoreapi.com/img/71li-ujtlUL._AC_UX679_.jpg",
        "stock": 500,
        "rating": {
            "rate": 4.7,
            "count": 500
        },
        "created_at": "2025-01-21",
        "updated_at": "2025-01-21",
        "supplier": "Menswear",
        "category": "men's clothing"
    },
    {
        "name": "Mens Casual Slim Fit",
        "description": "The color could be slightly different between on the screen and in practice. / Please note that body builds vary by person, therefore, detailed size information should be reviewed below on the product description.",
        "price": 15.99,
        "brand": "Casualwear",
        "image": "https://fakestoreapi.com/img/71YXzeOuslL._AC_UY879_.jpg",
        "stock": 430,
        "rating": {
            "rate": 2.1,
            "count": 430
        },
        "created_at": "2025-01-21",
        "updated_at": "2025-01-21",
        "supplier": "Casualwear",
        "category": "men's clothing"
    },
    {
        "name": "John Hardy Women's Legends Naga Gold & Silver Dragon Station Chain Bracelet",
        "description": "From our Legends Collection, the Naga was inspired by the mythical water dragon that protects the ocean's pearl. Wear facing inward to be bestowed with love and abundance, or outward for protection.",
        "price": 695,
        "brand": "John Hardy",
        "image": "https://fakestoreapi.com/img/71pWzhdJNwL._AC_UL640_QL65_ML3_.jpg",
        "stock": 400,
        "rating": {
            "rate": 4.6,
            "count": 400
        },
        "created_at": "2025-01-21",
        "updated_at": "2025-01-21",
        "supplier": "John Hardy",
        "category": "jewelery"
    },
    {
        "name": "Solid Gold Petite Micropave",
        "description": "Satisfaction Guaranteed. Return or exchange any order within 30 days. Designed and sold by Hafeez Center in the United States. Satisfaction Guaranteed. Return or exchange any order within 30 days.",
        "price": 168,
        "brand": "Gold Jewelry",
        "image": "https://fakestoreapi.com/img/61sbMiUnoGL._AC_UL640_QL65_ML3_.jpg",
        "stock": 70,
        "rating": {
            "rate": 3.9,
            "count": 70
        },
        "created_at": "2025-01-21",
        "updated_at": "2025-01-21",
        "supplier": "Hafeez Center",
        "category": "jewelery"
    },
    {
        "name": "White Gold Plated Princess",
        "description": "Classic Created Wedding Engagement Solitaire Diamond Promise Ring for Her. Gifts to spoil your love more for Engagement, Wedding, Anniversary, Valentine's Day...",
        "price": 9.99,
        "brand": "White Gold",
        "image": "https://fakestoreapi.com/img/71YAIFU48IL._AC_UL640_QL65_ML3_.jpg",
        "stock": 400,
        "rating": {
            "rate": 3,
            "count": 400
        },
        "created_at": "2025-01-21",
        "updated_at": "2025-01-21",
        "supplier": "White Gold",
        "category": "jewelery"
    },
    {
        "name": "Pierced Owl Rose Gold Plated Stainless Steel Double",
        "description": "Rose Gold Plated Double Flared Tunnel Plug Earrings. Made of 316L Stainless Steel",
        "price": 10.99,
        "brand": "Pierced Owl",
        "image": "https://fakestoreapi.com/img/51UDEzMJVpL._AC_UL640_QL65_ML3_.jpg",
        "stock": 100,
        "rating": {
            "rate": 1.9,
            "count": 100
        },
        "created_at": "2025-01-21",
        "updated_at": "2025-01-21",
        "supplier": "Pierced Owl",
        "category": "jewelery"
    },
    {
        "name": "WD 2TB Elements Portable External Hard Drive - USB 3.0",
        "description": "USB 3.0 and USB 2.0 Compatibility Fast data transfers Improve PC Performance High Capacity; Compatibility Formatted NTFS for Windows 10, Windows 8.1, Windows 7; Reformatting may be required for other operating systems; Compatibility may vary depending on user’s hardware configuration and operating system",
        "price": 64,
        "brand": "WD",
        "image": "https://fakestoreapi.com/img/61IBBVJvSDL._AC_SY879_.jpg",
        "stock": 203,
        "rating": {
            "rate": 3.3,
            "count": 203
        },
        "created_at": "2025-01-21",
        "updated_at": "2025-01-21",
        "supplier": "Western Digital",
        "category": "electronics"
    },
    {
        "name": "SanDisk SSD PLUS 1TB Internal SSD - SATA III 6 Gb/s",
        "description": "Easy upgrade for faster boot up, shutdown, application load and response (As compared to 5400 RPM SATA 2.5” hard drive; Based on published specifications and internal benchmarking tests using PCMark vantage scores) Boosts burst write performance, making it ideal for typical PC workloads The perfect balance of performance and reliability Read/write speeds of up to 535MB/s/450MB/s (Based on internal testing; Performance may vary depending upon drive capacity, host device, OS and application.)",
        "price": 109,
        "brand": "SanDisk",
        "image": "https://fakestoreapi.com/img/61U7T1koQqL._AC_SX679_.jpg",
        "stock": 470,
        "rating": {
            "rate": 2.9,
            "count": 470
        },
        "created_at": "2025-01-21",
        "updated_at": "2025-01-21",
        "supplier": "SanDisk",
        "category": "electronics"
    },
    {
        "name": "Silicon Power 256GB SSD 3D NAND A55 SLC Cache Performance Boost SATA III 2.5",
        "description": "3D NAND flash are applied to deliver high transfer speeds Remarkable transfer speeds that enable faster bootup and improved overall system performance. The advanced SLC Cache Technology allows performance boost and longer lifespan 7mm slim design suitable for Ultrabooks and Ultra-slim notebooks. Supports TRIM command, Garbage Collection technology, RAID, and ECC (Error Checking & Correction) to provide the optimized performance and enhanced reliability.",
        "price": 109,
        "brand": "Silicon Power",
        "image": "https://fakestoreapi.com/img/71kWymZ+c+L._AC_SX679_.jpg",
        "stock": 319,
        "rating": {
            "rate": 4.8,
            "count": 319
        },
        "created_at": "2025-01-21",
        "updated_at": "2025-01-21",
        "supplier": "Silicon Power",
        "category": "electronics"
    },
    {
        "name": "WD 4TB Gaming Drive Works with Playstation 4 Portable External Hard Drive",
        "description": "Expand your PS4 gaming experience, Play anywhere Fast and easy, setup Sleek design with high capacity, 3-year manufacturer's limited warranty",
        "price": 114,
        "brand": "WD",
        "image": "https://fakestoreapi.com/img/61mtL65D4cL._AC_SX679_.jpg",
        "stock": 400,
        "rating": {
            "rate": 4.8,
            "count": 400
        },
        "created_at": "2025-01-21",
        "updated_at": "2025-01-21",
        "supplier": "Western Digital",
        "category": "electronics"
    },
    {
        "name": "Acer SB220Q bi 21.5 inches Full HD (1920 x 1080) IPS Ultra-Thin",
        "description": "21. 5 inches Full HD (1920 x 1080) widescreen IPS display And Radeon free Sync technology. No compatibility for VESA Mount Refresh Rate: 75Hz - Using HDMI port Zero-frame design | ultra-thin | 4ms response time | IPS panel Aspect ratio - 16: 9. Color Supported - 16. 7 million colors. Brightness - 250 nit Tilt angle -5 degree to 15 degree. Horizontal viewing angle-178 degree. Vertical viewing angle-178 degree 75 hertz",
        "price": 599,
        "brand": "Acer",
        "image": "https://fakestoreapi.com/img/81QpkIctqPL._AC_SX679_.jpg",
        "stock": 250,
        "rating": {
            "rate": 2.9,
            "count": 250
        },
        "created_at": "2025-01-21",
        "updated_at": "2025-01-21",
        "supplier": "Acer",
        "category": "electronics"
    },
    {
        "name": "Samsung 49-Inch CHG90 144Hz Curved Gaming Monitor",
        "description": "49-inch ultra-wide curved gaming monitor with a 144Hz refresh rate and 1ms response time. G-SYNC and FreeSync support for smooth gaming performance. HDR support and Quantum Dot technology for vibrant colors.",
        "price": 999.99,
        "brand": "Samsung",
        "image": "https://images.samsung.com/is/image/samsung/p6pim/au/lc49hg90dmexxy/gallery/au-c49hg90-lc49hg90dmexxy-530482141?$684_547_PNG$",
        "stock": 150,
        "rating": {
            "rate": 4.7,
            "count": 150
        },
        "created_at": "2025-01-21",
        "updated_at": "2025-01-21",
        "supplier": "Samsung",
        "category": "electronics"
    },
    {
        "name": "Amazon Echo (3rd Gen) Smart speaker with Alexa",
        "description": "Meet the all-new Echo with a fabric design and improved sound. Ask Alexa to play music, answer questions, check the weather, control smart home devices, and more.",
        "price": 99.99,
        "brand": "Amazon",
        "image": "https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcSoQYavO6G1_BlmTwTqNqII3UkOfbObnUTcp8dm5LtVGUYbWOh_6MotPWSo5j-In_OPBx2jQMlPkTJCDmU2aXpo1ycu7XKR-mEiezU2Ps7epsKZ8XtxDlFQ2N2VvIik9qWBUrrwHg&usqp=CAc",
        "stock": 200,
        "rating": {
            "rate": 4.5,
            "count": 200
        },
        "created_at": "2025-01-21",
        "updated_at": "2025-01-21",
        "supplier": "Amazon",
        "category": "electronics"
    },
    {
        "name": "Rain Jacket Women Windbreaker Striped Climbing Jacket",
        "description": "Lightweight material, suitable for long-time outdoor activities. Excellent Windbreaker and water resistant, more breathable, for all seasons in your lifestyle.",
        "price": 39.99,
        "brand": "Rain Jacket",
        "image": "https://m.media-amazon.com/images/I/517nGPKF-8L.SS700.jpg",
        "stock": 170,
        "rating": {
            "rate": 3.8,
            "count": 170
        },
        "created_at": "2025-01-21",
        "updated_at": "2025-01-21",
        "supplier": "Rain Jacket",
        "category": "women's clothing"
    },
    {
        "name": "PUMA Women's Essential Woven Jacket",
        "description": "Slightly lightweight, yet with durability, and an excellent option for outdoor activities like running, jogging, or cycling.",
        "price": 22.98,
        "brand": "PUMA",
        "image": "https://img.tatacliq.com/images/i18//437Wx649H/MP000000023054705_437Wx649H_202407261707101.jpeg",
        "stock": 285,
        "rating": {
            "rate": 3.7,
            "count": 285
        },
        "created_at": "2025-01-21",
        "updated_at": "2025-01-21",
        "supplier": "PUMA",
        "category": "women's clothing"
    },
    {
        "name": "Under Armour Women's ColdGear Reactor 1/2 Zip",
        "description": "Soft, ultra-warm, and water-resistant with breathable material to help manage moisture.",
        "price": 49.99,
        "brand": "Under Armour",
        "image": "https://m.media-amazon.com/images/I/61C-2N4mveL._SX679_.jpg",
        "stock": 200,
        "rating": {
            "rate": 4.2,
            "count": 200
        },
        "created_at": "2025-01-21",
        "updated_at": "2025-01-21",
        "supplier": "Under Armour",
        "category": "women's clothing"
    },
    {
        "name": "Women's Athletic Tank Top",
        "description": "The perfect workout tank top that pairs with any bottom and keeps you cool and comfortable.",
        "price": 14.99,
        "brand": "Under Armour",
        "image": "https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcR7SwZpUKXDvntqZO7rv25M5bU9gghuWulPny7oC56j87n7ezB8yNYYBQMXj4LlvmZCohXuq_VIxGRsSYqeVs5dJT0dn5PM6gmiCxdZv0s",
        "stock": 370,
        "rating": {
            "rate": 4.4,
            "count": 370
        },
        "created_at": "2025-01-21",
        "updated_at": "2025-01-21",
        "supplier": "Under Armour",
        "category": "women's clothing"
    },
    {
        "name": "Samsung 49-Inch CHG90 144Hz Curved Gaming Monitor (LC49HG90DMNXZA) – Super Ultrawide Screen QLED",
        "description": "49 INCH SUPER ULTRAWIDE 32:9 CURVED GAMING MONITOR with dual 27 inch screen side by side QUANTUM DOT (QLED) TECHNOLOGY, HDR support and factory calibration provides stunningly realistic and accurate color and contrast 144HZ HIGH REFRESH RATE and 1ms ultra fast response time work to eliminate motion blur, ghosting, and reduce input lag",
        "price": 999.99,
        "brand": "Samsung",
        "image": "https://fakestoreapi.com/img/81Zt42ioCgL._AC_SX679_.jpg",
        "stock": 140,
        "rating": 2.2,
        "created_at": "2025-01-21",
        "updated_at": "2025-01-21",
        "supplier": "Samsung",
        "category": "electronics"
    },
    {
        "name": "BIYLACLESEN Women's 3-in-1 Snowboard Jacket Winter Coats",
        "description": "Note:The Jackets is US standard size, Please choose size as your usual wear Material: 100% Polyester; Detachable Liner Fabric: Warm Fleece. Detachable Functional Liner: Skin Friendly, Lightweigt and Warm.Stand Collar Liner jacket, keep you warm in cold weather. Zippered Pockets: 2 Zippered Hand Pockets, 2 Zippered Pockets on Chest (enough to keep cards or keys)and 1 Hidden Pocket Inside.Zippered Hand Pockets and Hidden Pocket keep your things secure. Humanized Design: Adjustable and Detachable Hood and Adjustable cuff to prevent the wind and water,for a comfortable fit. 3 in 1 Detachable Design provide more convenience, you can separate the coat and inner as needed, or wear it together. It is suitable for different season and help you adapt to different climates",
        "price": 56.99,
        "brand": "BIYLACLESEN",
        "image": "https://fakestoreapi.com/img/51Y5NI-I5jL._AC_UX679_.jpg",
        "stock": 235,
        "rating": 2.6,
        "created_at": "2025-01-21",
        "updated_at": "2025-01-21",
        "supplier": "BIYLACLESEN",
        "category": "women's clothing"
    },
    {
        "name": "Lock and Love Women's Removable Hooded Faux Leather Moto Biker Jacket",
        "description": "100% POLYURETHANE(shell) 100% POLYESTER(lining) 75% POLYESTER 25% COTTON (SWEATER), Faux leather material for style and comfort / 2 pockets of front, 2-For-One Hooded denim style faux leather jacket, Button detail on waist / Detail stitching at sides, HAND WASH ONLY / DO NOT BLEACH / LINE DRY / DO NOT IRON",
        "price": 29.95,
        "brand": "Lock and Love",
        "image": "https://fakestoreapi.com/img/81XH0e8fefL._AC_UY879_.jpg",
        "stock": 340,
        "rating": 2.9,
        "created_at": "2025-01-21",
        "updated_at": "2025-01-21",
        "supplier": "Lock and Love",
        "category": "women's clothing"
    }
]


    for product_data in sample_products:
        # Ensure supplier exists
        supplier, _ = Supplier.objects.get_or_create(name=product_data["supplier"])

        # Ensure category exists
        category, _ = Category.objects.get_or_create(name=product_data["category"])

        # Create product with all fields except image
        product, created = Product.objects.get_or_create(
            name=product_data["name"],
            defaults={
                "description": product_data["description"],
                "price":  82 * product_data["price"],
                "brand": product_data["brand"],
                "stock": product_data["stock"],
                "created_at": product_data["created_at"],
                "updated_at": product_data["updated_at"],
                "category": category,
                "supplier": supplier,
            }
        )

        # Handle image if provided and the product is newly created
        if created and "image" in product_data:
            image_url = product_data["image"]
            try:
                response = requests.get(image_url)
                if response.status_code == 200:
                    product.image.save(
                        os.path.basename(image_url),
                        ContentFile(response.content),
                        save=True
                    )
            except Exception as e:
                print(f"Error downloading image for product {product.name}: {e}")
