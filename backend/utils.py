import requests
import maxminddb

BOT_AGENTS = ["Googlebot", "Bingbot", "Facebook", "Applebot", "Microsoft"]

def detect_bot(user_agent: str) -> bool:
    return any(bot in user_agent for bot in BOT_AGENTS)

def get_client_ip(request):
    return request.client.host

def get_country_from_ip(ip):
    with maxminddb.open_database("GeoLite2-Country.mmdb") as reader:
        response = reader.get(ip)
        return response.get("country", {}).get("iso_code", "")

def get_ip_info_online(ip):
    """Use an external API if GeoLite2 is not available."""
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        return response.json()
    except:
        return None