import requests
import json
import re
from tqdm import tqdm

#教学链接：https://www.bilibili.com/video/BV1hm4y1n7u8/?spm_id_from=333.337.search-card.all.click&vd_source=ab498dab89fca199b1fa3419b6569ca3


import requests
cookies = {
    'pgv_pvid': '2081590094',
    'Qs_lvt_323937': '1670587159%2C1684252729',
    'Qs_pv_323937': '3585644883378599400%2C1695137569189352200',
    'qq_domain_video_guid_verify': 'bf87c4d81e15528a',
    '_qimei_uuid42': '1821715233a100fdedfca046cf85c3c265e07530d1',
    '_qimei_fingerprint': 'dc9ac778ca4a0d5c5ac6719cf470d572',
    '_qimei_q36': '',
    '_qimei_h38': '19c59f29edfca046cf85c3c202000002018217',
    'o_minduid': 'ZQdj3lH-jcdsosze3I9JH1QunYy2unqh',
    'RK': 'LbvwBY/TWH',
    'ptcz': '90524a2dd0dd9a756b3f3624f3ed9f00100471204883ce20dd5a2a70d2f98af7',
    'ad_session_id': '433f26i57nl3u',
    'pgv_info': 'ssid=s6302966394',
    'vversion_name': '8.2.95',
    'video_omgid': 'bf87c4d81e15528a',
    'LPVLturn': '277',
    'LPSJturn': '500',
    'LVINturn': '448',
    'LPHLSturn': '554',
    'LDERturn': '499',
    'LPPBturn': '30',
    'LPDFturn': '791',
    'appuser': 'C39F855485ADA8DE',
    'LZTturn': '106',
    'ufc': 'r64_1_1709963119',
}

headers = {
    'authority': 'vd6.l.qq.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'text/plain;charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'pgv_pvid=2081590094; Qs_lvt_323937=1670587159%2C1684252729; Qs_pv_323937=3585644883378599400%2C1695137569189352200; qq_domain_video_guid_verify=bf87c4d81e15528a; _qimei_uuid42=1821715233a100fdedfca046cf85c3c265e07530d1; _qimei_fingerprint=dc9ac778ca4a0d5c5ac6719cf470d572; _qimei_q36=; _qimei_h38=19c59f29edfca046cf85c3c202000002018217; o_minduid=ZQdj3lH-jcdsosze3I9JH1QunYy2unqh; RK=LbvwBY/TWH; ptcz=90524a2dd0dd9a756b3f3624f3ed9f00100471204883ce20dd5a2a70d2f98af7; ad_session_id=433f26i57nl3u; pgv_info=ssid=s6302966394; vversion_name=8.2.95; video_omgid=bf87c4d81e15528a; LPVLturn=277; LPSJturn=500; LVINturn=448; LPHLSturn=554; LDERturn=499; LPPBturn=30; LPDFturn=791; appuser=C39F855485ADA8DE; LZTturn=106; ufc=r64_1_1709963119',
    'origin': 'https://v.qq.com',
    'pragma': 'no-cache',
    'referer': 'https://v.qq.com/',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

data = '{"buid":"vinfoad","vinfoparam":"charge=0&otype=ojson&defnpayver=3&spau=1&spaudio=0&spwm=1&sphls=2&host=v.qq.com&refer=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmzc00200zm1aje0%2Fz0048qql7p4.html&ehost=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmzc00200zm1aje0%2Fz0048qql7p4.html&sphttps=1&encryptVer=9.2&cKey=lhnhQDI7yd_1Ic1Orq2-LnCjnpb8Ocr0cPTcLzq7zEul_f4uOWcoU2JPR8Gi77I5NRJC2kNPkmr5Cp7VHCeQghpmp7rG5tiHjLv_PnnatnPaZfOXktuBpd_IguNq9o6Q2V37_IMO6YAnFjOj-NmZhE-NjjawCzIdF66cdsFdzz5jk70UOmynTHDptaxqIemxrSlkg-M_BbDaBoWwiX7uSsBkDK_qlv9BvC71ChrA2gKogC-Pt8O57nCcynqx0Guf2MPBftXrjbMV7ievoL0n6v0sy32WbBTqw_Ha7FV8BMVsJufzmp6-sOuwl7W96tlGKIoknsNiqoS2Pr6xyJY7l74Vw5nuc_ZZdbexbqxY2JGA5FYOLyYXmeoaETQAnQJ9XuxlPuZCOro_ib05hp54kv2wbIfJv8vr4VeZg4d3t5pbgsLJOwaTiqamtC_stvRCduvh8iedI5gAQA4woDzPzBRM--yI5mkqDNDiSImmJp2fC7Thy8xZSScftT1tdUi66bweRyYDAwMBT1OO&clip=4&guid=bf87c4d81e15528a&flowid=ca150712240539658e6f64958f95cd4b&platform=10201&sdtfrom=v1010&appVer=1.31.1&unid=&auth_from=&auth_ext=&vid=z0048qql7p4&defn=uhd&fhdswitch=0&dtype=3&spsrt=2&tm=1709963113&lang_code=0&logintoken=%7B%22access_token%22%3A%22557BB9DAE45CBC031FA95C20D215C10E%22%2C%22appid%22%3A%22101483052%22%2C%22vusession%22%3A%22ipWtmthO9LeZWEfw9KiD1w.M%22%2C%22openid%22%3A%22D9B8A370FD02E0629339064E8A5A515A%22%2C%22vuserid%22%3A%22326778436%22%2C%22video_guid%22%3A%22bf87c4d81e15528a%22%2C%22main_login%22%3A%22qq%22%7D&spvvpay=1&spadseg=3&spav1=15&hevclv=28&spsfrhdr=0&spvideo=0&spm3u8tag=67&spmasterm3u8=3&drm=40","sspAdParam":"{\\"ad_scene\\":1,\\"pre_ad_params\\":{\\"ad_scene\\":1,\\"user_type\\":2,\\"video\\":{\\"base\\":{\\"vid\\":\\"z0048qql7p4\\",\\"cid\\":\\"mzc00200zm1aje0\\"},\\"is_live\\":false,\\"type_id\\":2,\\"referer\\":\\"https://v.qq.com/\\",\\"url\\":\\"https://v.qq.com/x/cover/mzc00200zm1aje0/z0048qql7p4.html\\",\\"flow_id\\":\\"ca150712240539658e6f64958f95cd4b\\",\\"refresh_id\\":\\"\\",\\"fmt\\":\\"fhd\\"},\\"platform\\":{\\"guid\\":\\"bf87c4d81e15528a\\",\\"channel_id\\":0,\\"site\\":\\"web\\",\\"platform\\":\\"in\\",\\"from\\":0,\\"device\\":\\"pc\\",\\"play_platform\\":10201,\\"pv_tag\\":\\"www_baidu_com|v_qq_com\\",\\"support_click_scan_integration\\":true},\\"player\\":{\\"version\\":\\"1.31.1\\",\\"plugin\\":\\"3.4.49\\",\\"switch\\":1,\\"play_type\\":\\"0\\"},\\"token\\":{\\"type\\":1,\\"vuid\\":326778436,\\"vuser_session\\":\\"ipWtmthO9LeZWEfw9KiD1w.M\\",\\"app_id\\":\\"101483052\\",\\"open_id\\":\\"D9B8A370FD02E0629339064E8A5A515A\\",\\"access_token\\":\\"557BB9DAE45CBC031FA95C20D215C10E\\"}}}","adparam":"adType=preAd&vid=z0048qql7p4&sspKey=docn"}'

response = requests.post('https://vd6.l.qq.com/proxyhttp', cookies=cookies, headers=headers, data=data)


print(response.text)

vinfo=response.json()['vinfo']
#print(vinfo)
json_data=json.loads(vinfo)
#print(json_data)
m3u8_text=json_data['vl']['vi'][0]['ul']['m3u8']
#print(m3u8_text)
# 将所有#E开头的内容匹配并去掉
m3u8_text=re.sub('#E.*','',m3u8_text)
#print(m3u8_text)
ts_list=m3u8_text.split()
#print(ts_list)

for ts in tqdm(ts_list):
    ts_url='https://ltscsy.qq.com/B_XztNc2Ue3HgxgyyNa2AR9ZuKsi3gn5Yu2qRaHu48Ro9ba59o4beSGptSRiV8hJbK/svp_50112/2uSuCSi9kzjNrclgaqIGXBjDQSKYOrc4DPS0AdEBh8W7XP_mGVBWTY1Yi3jmwPBL2MoN_qcB67VBBkUtxxemRk-BJabQ7DdmMpkLnl47ST5Z5Kn5kPFlXu7LtSGQk4Qy1q4jRgH2H3Bp1D2zq7BaLU_2Bl9vL5jrfi0tYU46VXUWnHomE5uNyYyXka7fZD0J1jMJ1EX6eyd5PWJgvh4OlR6CDIwVq8w7R5TIr77lHB4YIWsE-ZNwLA/00_gzc_1000102_0b53gqajuaaaa4ajx5622ns4angdti4abhsa.f322016.1.ts?index=0&start=0&end=11040&brs=0&bre=1606835&ver=4&token=c339c4bfed1bc46f3914bfd1301066db'+ts
    ts_data=requests.get(ts_url).content
    open('猎冰1.mp4',mode='ab').write(ts_data)

