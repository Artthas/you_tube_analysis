'use client';

import React, { useContext } from 'react';
import { GlobalContext } from '@/context';
import Image from 'next/image';
import Link from 'next/link';
import styles from '../styles/components/search-result.module.scss';
import Loading from './loading';

export default function SearchResult() {

  const { state: { searchResult, isResultLoading } } = useContext(GlobalContext);

  return isResultLoading ? (
      <Loading/>
    ) : (
      searchResult.length === 0 ? (
        <></>
      ) : (
        <ul className={styles['main']}>
          {searchResult.map((item) =>
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
    )
}
