'use client';

import React, { useContext } from 'react';
import { GlobalContext } from '@/context';
import Image from 'next/image';
import Link from 'next/link';
import styles from '../styles/components/search-result.module.scss';

export default function SearchResult() {

  const { state: { searchResult } } = useContext(GlobalContext);

  const searchResultMock = [
    {
      channel_text: "Px Jama",
      channel_url: "https://www.youtube.com/@pxjama",
      published_time: "9 months ago",
      thumbnail_360x202: "https://i.ytimg.com/vi/PFxZQR1KUWc/hq720_2.jpg?sqp=-oaymwE2COgCEMoBSFXyq4qpAygIARUAAIhCGABwAcABBvABAfgBzgWAAoAKigIMCAAQARhlIEwoPzAP&rs=AOn4C…",
      thumbnail_720x404: "https://i.ytimg.com/vi/PFxZQR1KUWc/hq720_2.jpg?sqp=-oaymwE2CNAFEJQDSFXyq4qpAygIARUAAIhCGABwAcABBvABAfgBzgWAAoAKigIMCAAQARhlIEwoPzAP&rs=AOn4C…",
      title_label: "Учил python 30 дней. Полное видео на канале by Px Jama 9 months ago 1 minute 1,742,032 views - play Short",
      title_text: "Учил python 30 дней. Полное видео на канале",
      video_length: "1:00",
      video_url: "https://www.youtube.com/shorts/PFxZQR1KUWc",
      view_count: "1,742,032 views"
    },{
      channel_text: "Роман Сакутин - GameDev",
      channel_url: "https://www.youtube.com/@rsakutin",
      published_time: "7 months ago",
      thumbnail_360x202: "https://i.ytimg.com/vi/w8rRhAup4kg/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAWyMR-N7WTa-E0JLX2RzTitmVSYQ",
      thumbnail_720x404: "https://i.ytimg.com/vi/w8rRhAup4kg/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLB21yNO2tNEThov-DSw1XTHghCc0Q",
      title_label: "C# 2023 С НУЛЯ ДО ПРОФИ | СЛИВ ЛУЧШЕГО КУРСА by Роман Сакутин - GameDev 7 months ago 9 hours, 19 minutes 1,089,307 views",
      title_text: "C# 2023 С НУЛЯ ДО ПРОФИ | СЛИВ ЛУЧШЕГО КУРСА",
      video_length: "9:19:56",
      video_url: "https://www.youtube.com/watch?v=w8rRhAup4kg&pp=ygXzA9C_0YDQvtCz0YDQsNC80LzQuNGA0L7QstCw0L3QuNC1INGBINC90YPQu9GPIHwg0L_RgNC-0LPRgNCw0LzQvNC40…",
      view_count: "1,089,307 views"
    },{
      channel_text: "Хьюстон у нас проблемы !",
      channel_url: "https://www.youtube.com/@HSTNproblem",
      published_time: "11 months ago",
      thumbnail_360x202: "https://i.ytimg.com/vi/8GX-zsr8lIc/hq720_2.jpg?sqp=-oaymwE2COgCEMoBSFXyq4qpAygIARUAAIhCGABwAcABBvABAfgBzgWAAoAKigIMCAAQARhQIF0oZTAP&rs=AOn4C…",
      thumbnail_720x404: "https://i.ytimg.com/vi/8GX-zsr8lIc/hq720_2.jpg?sqp=-oaymwE2CNAFEJQDSFXyq4qpAygIARUAAIhCGABwAcABBvABAfgBzgWAAoAKigIMCAAQARhQIF0oZTAP&rs=AOn4C…",
      title_label: "Почему программисты работают по ночам by Хьюстон у нас проблемы ! 11 months ago 17 seconds 1,063,959 views - play Short",
      title_text: "Почему программисты работают по ночам",
      video_length: "0:17",
      video_url: "https://www.youtube.com/shorts/8GX-zsr8lIc",
      view_count: "1,063,959 views"
    }
  ]

  return (
    <ul className={styles['main']}>
      {searchResult?.map((item) =>
        <li className={styles['main-item']} key={item?.title_text}>
          <Link className={styles['main-item-link']} href={item?.video_url}>
            <Image
              className={styles['main-image']}
              src={item?.thumbnail_360x202}
              width={250}
              height={150}
              alt="Preview"
            />
          </Link>
          <div className={styles['main-info']}>
            <Link className={styles['main-title']} href={item?.video_url}>{item.title_text}</Link>
            <p className={styles['main-inner']}>{item.view_count} • {item.published_time}</p>
            <Link className={styles['main-channel-name']} href={item?.channel_url}><span>Channel:</span>{item.channel_text}</Link>
          </div>
        </li>
      )}
    </ul>
  )
}
