import requests

cookies = {
    'GPS': '1',
    'YSC': '7kN4kGqB0p4',
    'VISITOR_INFO1_LIVE': '4tZdkTdahpM',
    'PREF': 'f4=4000000&tz=Europe.Belgrade',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'X-Goog-Request-Time': '1690376690301',
    'Content-Type': 'application/json',
    'X-Goog-Visitor-Id': 'Cgs0dFpka1RkYWhwTSiws4SmBg%3D%3D',
    'Content-Encoding': 'gzip',
    'X-YouTube-Client-Name': '1',
    'X-YouTube-Client-Version': '2.20230725.01.00',
    'X-YouTube-Device': 'cbr=Firefox&cbrver=115.0&ceng=Gecko&cengver=109.0&cos=X11&cplatform=DESKTOP',
    'X-YouTube-Page-CL': '550787316',
    'X-YouTube-Page-Label': 'youtube.desktop.web_20230725_01_RC00',
    'X-YouTube-Utc-Offset': '120',
    'X-YouTube-Time-Zone': 'Europe/Belgrade',
    'X-YouTube-Ad-Signals': 'dt=1690376625598&flash=0&frm&u_tz=120&u_his=2&u_h=864&u_w=1536&u_ah=837&u_aw=1536&u_cd=24&bc=31&bih=750&biw=930&brdim=0%2C27%2C0%2C27%2C1536%2C27%2C1536%2C837%2C930%2C750&vis=2&wgl=true&ca_type=image',
    'Origin': 'https://www.youtube.com',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://www.youtube.com/@chestniyblog/videos',
    # 'Cookie': 'GPS=1; YSC=7kN4kGqB0p4; VISITOR_INFO1_LIVE=4tZdkTdahpM; PREF=f4=4000000&tz=Europe.Belgrade',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'alt': 'json',
    'key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
}

data = '\x1f\x8b\b\x00\x00\x00\x00\x00\x00\x03\xad\x95k\x8f¢H\x14\x86ÿJ\x87d\x93Ýdº\x87B¥µçSsU¡@.\x85Êfc\x10P\x8a«\x02\x8aÍdþûVÑNOg³\x1f\'\x91¤êáÜê=\x94ç;\x13Ve\x1bßZæå;\x13æ8.\x87U\x923/L}a¾0Gº\x822Y½¿5\x82"f^ÀÏ\xad\x17×\r®JbÃ=q,7b\x9f¹É\x13\v\x9eX\x96zTå\x01\x1f\x17å¡¢1\x83ÓiQ6m\x90çRÐ\x06ÄCÔÅ>Ñ¶ªlð\\Ý!\vÇø"Øb\n´©"C=Þ%\v«\x85ÅU°¥èv&L_\x17Ô.ÓLÂÄUÇ\x13¶º\x96gáh¥zLYÓR\x06ñ\x94Ú\x15\xadJ}1ÐÆ\x8a¬\x952eÓ3¦\x8c¿\x0eñ°^\x1f\x91ÅOL\x9awS\a\x84-ö>Í\x9bÂ\vµ+/\x83ÝÜ£¾×}@íòî:vd³\x96(ÛÕkj\aG<Éaô+Êò\x86§µ\b\'\x1aÏ\\\x994ÞóY£vR»#¾z:Ä\x9bè«G9\x91àÀ\f\'¡l¬\aC¼\x9aæX>ï©ï£Ns\x88rKk1.Wjw®uâ+Z==ïR×\x87ZB\x8eú\x02L\x99)\x9e\tûc$\r}È#qèÅ\x7f\x9579¾¶>\x14\x98µgr\nSGT\x95ã¥¸|D[ª\x9bOÊßO\x86«O\x8a\x1eÏ´ºeÜRöÞ\r)\x19Ô»w£\x83ôdâá6tm\x05\x7fU|?Å]½.\x12)\vX\x9a\x03Ö.eÕÌ¡ì\x06(»«\x97¶4oõf¡ÉÈæ\x16co\x8d:O\x11tw\x9d¸\x9eg\x88¡blPé©!°U[Í+/\x17N\x10-G¾\x9awQîÙæ\x86ìK{\x83Ô\x10ÃL1#6Â¦âåP±-\x87\x05\x15\x02\x9ek\x95\x82ë\x81%°K\x03Ù\x99}\n\x14ß\n\\E\x8c8û\x14Î}\x0f¹y\x17¸KÖ\x03B©e\x82d!àº²ÜyEÔm×3!ä¢Í\x86<~¶\\\x9a\x8aqA\x1b\x85·Ö³¥\x8d|Ç\x06F\x19É\x8a\x11öBá¬oÂ6Wæa\x91d\x90\x03º/wlÀMÎ\x06×*÷þÍ\x83&ùo÷\x12È\x1aî\x823Ò\x050]«3zx\x83Ò\x11\x98R6Qï60]\nn\x19Í·iâù®\x80\x90Ln°bx\x88]v\bDN\x84üÞ\x93}9X\'k¤f7«\x8c²`#p\x9e\'OB5{\x8b\x94Èòûß¡r$Z²Aä4\xa0å\nk\x7f$${Vé}\x10\x1dÈSXY6FÜÄ\x0e7\'aÏæ\x8a\x9d/ç\x88\x8bX¢h\x0fU\x7f¹\x97\x15\x8cPô\x16¨V¿GmæJv½/ªQÀÞ¿ñ¤jÿW"ëf¸\x16\vÓE\aÝã\x04¦[\x16ºÙ\x980\x00o¸kÆN!`\x8c&«ÎÑ\x8c\x8b»³\x17Õ\xadÖg2ÆçvÅ:\x9a¶±(+OóGÂ\x82ú0v´åA#×²\x1a5Ï\x84¥iO®ªf¸\x1eeI[R»\r7Ø\r×·z3zÊÒ\x11eF\x1aQÖµÄ7]ü\x8e\x8f\x97ÿ\x1d\x1f¯\x95¾\x7f¼\x8e\x1avn1cýÔW·©}\x88×\x91\x04Ù\x99ãyÇ~\vf\x92-·§m¦\\£Ò\x13¶À°-4[ ¤\x94+\x97¥møñ\x85¹4qýz\x1cÆ\b\x03«\x1eçyð\x95L\x84\x87?7\x00|{@ûKÙ^¾=è¸¼Ü\x1enS~Ç\x8f¿=Ô×\x17ÀÎ\x9eØ¿\x1eÔ8Ìª¯\x1c\vXò\x03\x0f\n®ãCuû\n\x00\tA\x9aÜ\x84u\x1c\x97R\\6¸}Sò*\xa0YÀ\x137!ï\x8a\x00\x97¯§Ó:Þÿ\x1c8]¼\x97psÊ\x837XEdh1kYØI\vg¥¿nwÐ\x94ä\x9d`\x9bkG¶iÝûºêHéïã\x8d¹\'f>ø¯9÷³\x96ª¹Û\x92\x83\x91-IÓ\x1eªº @\x92\x1dÍ5WÌ\x0f\x126¾\x12)\x1aæåïïïK\x17\x171${ÀÏØÑ3ÏsSþyö\x85ÎÆ\x1c\x87AKR8mP·qD\x0f@\x86e\x8bCñÓ\x80>]Äª\x8e\x89ÿ\x94\x06ÿ4ºó\xa0i_Cò\x97H\x84¡ñ\x99G@òÿC$\x8bk\x1cä¸\x8f#q\x18Ø2\xadbñ\x1eþãÕ\ad\x1a¡\x14|ãy®\x9d\x8a\x88\x8f\x9aU_qìãkõ1þÅ\x8a40®é¼\x1fO§$Å¿F\x94kÿA\b\x00\x00'.encode()

response = requests.post('https://www.youtube.com/youtubei/v1/log_event', params=params, cookies=cookies, headers=headers, data=data)