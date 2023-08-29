'use client';

import React, { useContext } from 'react';
import { GlobalContext } from '@/context';
import Image from 'next/image';
import Link from 'next/link';
import styles from '../styles/components/search-result.module.scss';
import Loading from './loading';

export default function SearchResult() {

  const { state: { searchResult, isResultLoading, isResultLoadingError } } = useContext(GlobalContext);

  const { main_channel, concurrent_channels } = searchResult;

  if (isResultLoading) {
    return <Loading />;
  }

  if (isResultLoadingError) {
    return <div className={styles['error-message']}>An error occurred while loading the results. Please try again.</div>;
  }

  if (main_channel.channel_name.length === 0) {
    return <></>;
  }

  return (
    <section className={styles['main']}>
      {/* <ul className={styles['main-video-list']}>
        {searchResult.videos_from_first_channel.map((item) =>
          <li className={styles['main-video-item']} key={item?.url}>
            <div className={styles['main-video-item-wrapper']}>
              <Link className={styles['main-video-link']} href={item?.url}>
                <Image
                  className={styles['main-video-image']}
                  src={item?.thumbnail}
                  width={250}
                  height={150}
                  alt="Preview"
                />
                <p className={styles['main-video-title']}>{item.title}</p>
              </Link>
            </div>
          </li>
        )}
      </ul> */}
      <ul className={styles['main-idea-list']}>
        {main_channel.ideas_by_top_new.map((item) =>
          <li className={styles['main-idea-item']} key={item?.Description}>
            <div className={styles['main-idea-item-wrapper']}>
              <p>Titles:</p>
              <p>
                <span>- {item['Main Title']}</span>
                <span>- {item['Alternative Title 1']}</span>
                <span>- {item['Alternative Title 2']}</span>
              </p>
              <p>Description:</p>
              <p>{item.Description}</p>
            </div>
          </li>
        )}
      </ul>
      <ul className={styles['main-idea-list']}>
        {main_channel.ideas_by_top_popular.map((item) =>
          <li className={styles['main-idea-item']} key={item?.Description}>
            <div className={styles['main-idea-item-wrapper']}>
              <p>Titles:</p>
              <p>
                <span>- {item['Main Title']}</span>
                <span>- {item['Alternative Title 1']}</span>
                <span>- {item['Alternative Title 2']}</span>
              </p>
              <p>Description:</p>
              <p>{item.Description}</p>
            </div>
          </li>
        )}
      </ul>
      <ul className={styles['main-idea-list']}>
        {concurrent_channels.ideas_by_top_new.map((item) =>
          <li className={styles['main-idea-item']} key={item?.Description}>
            <div className={styles['main-idea-item-wrapper']}>
              <p>Titles:</p>
              <p>
                <span>- {item['Main Title']}</span>
                <span>- {item['Alternative Title 1']}</span>
                <span>- {item['Alternative Title 2']}</span>
              </p>
              <p>Description:</p>
              <p>{item.Description}</p>
            </div>
          </li>
        )}
      </ul>
      <ul className={styles['main-idea-list']}>
        {concurrent_channels.ideas_by_top_popular.map((item) =>
          <li className={styles['main-idea-item']} key={item?.Description}>
            <div className={styles['main-idea-item-wrapper']}>
              <p>Titles:</p>
              <p>
                <span>- {item['Main Title']}</span>
                <span>- {item['Alternative Title 1']}</span>
                <span>- {item['Alternative Title 2']}</span>
              </p>
              <p>Description:</p>
              <p>{item.Description}</p>
            </div>
          </li>
        )}
      </ul>
    </section>
  );
}
