GrabConfig = {
    "SSD_cheap_600rub_allregions" : {
        "enable" : True,
        "url" : "https://www.avito.ru/all/tovary_dlya_kompyutera/komplektuyuschie/zhestkie_diski-ASgBAgICAkTGB~pm7gmwZw?d=1&q=kingston+ssd&s=104",
        # "url" : "https://www.avito.ru/all/tovary_dlya_kompyutera/komplektuyuschie/zhestkie_diski-ASgBAgICAkTGB~pm7gmwZw?cd=1&d=1&f=ASgBAgECAkTGB~pm7gmwZwFFxpoME3siZnJvbSI6MCwidG8iOjYwMH0&q=ssd&s=104",
        "title_exclude":{
            "Переходник", "Салазки", "Винт", "Болты", "Адаптер", "Корпус", "Комплект", "Крепления", "Шлейф", "Контейнер"
        },
        "exclude_composite" : True,
        "url_call_rand_delay" : {
            "page" : (3, 1.5),
            "item" : (3, 1.5)
        }
    }
}