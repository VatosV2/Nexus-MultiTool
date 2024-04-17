from Helper import *
from Helper.Common.utils import *

def download_images(url, folder_path):
    page_num = 1
    while True:
        response = requests.get(url, params={"page": page_num})
        soup = BeautifulSoup(response.content, 'html.parser')
        image_elements = soup.find_all('img')
        
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        for img in image_elements:
            img_url = img.get('src')
            if img_url:
                if not bool(urlparse(img_url).netloc):
                    img_url = urljoin(url, img_url)
                
                img_name = os.path.basename(img_url)
                
                img_path = os.path.join(folder_path, img_name)
                urlretrieve(img_url, img_path)
                print(f"{lc} Downloaded: {img_path}")
        
        next_page = soup.find('a', {'class': 'GrowthUnauthPinPaginationButton'})
        if next_page:
            url = urljoin(url, next_page['href'])
            page_num += 1
        else:
            break

def scrape_Avatars():
    new_title("Picture scraper discord.gg/nexustools")
    count = 0
    folder_choice = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] 1 Preset Folder Or 2 Ouput/Avatars Folder? (1/2): ")
    if folder_choice == "1":
        folder_path = "Data/Avatars/Preset"
    elif folder_choice == "2":
        folder_path = "Output/Avatars"
    else:
        folder_path = "Data/Avatars/Preset"
        print(f"{lc} Using Default: {folder_path}")
    
        
    urls = ['https://in.pinterest.com/Sarcaeus/anime-profile-pictures/', 'https://www.pinterest.com/noleafcloverr/anime-pfp/', 'https://www.pinterest.com/roslis528/cute-anime-girl/', 'https://www.pinterest.com/beeis47/anime-pfps/', 'https://www.pinterest.com/FlashiestGod/emo-pfps/', 'https://www.pinterest.com/astxrism_moon1/emo-pfps/', 'https://www.pinterest.de/dk2717/anime-profile-pictures/', 'https://www.pinterest.de/vxrliebte/cute-profile-pictures/', 'https://www.pinterest.de/vibesamurai/matching-profile-pictures/', 'https://www.pinterest.de/Wumo_/male-anime-profile-pics/' ]
    for url in urls:
        count += 1
        pinterest_url = url
        print(f"{lc} {count}/10 Url: {pinterest_url}")
        download_images(pinterest_url, folder_path)
    input("Press Enter To continue...")