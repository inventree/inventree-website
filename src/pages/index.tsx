import clsx from 'clsx';

import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';
import Heading from '@theme/Heading';

import ImageGallery from '@site/src/components/ImageGallery';


import ProjectStats from '@site/src/components/HomepageFeatures/ProjectStats';


import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className="hero__title">
          {siteConfig.title}
        </Heading>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
      </div>
    </header>
  );
}





export default function Home(): JSX.Element {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`${siteConfig.title}`}
      description="InvenTree - Intuitive Inventory Management">
      <HomepageHeader />
      <main>
        <HomepageFeatures />
        {false && <ImageGallery 
              images={[
                {src: 'img/webgallery/bom_add_item.png', title: 'Add a new BOM item'},
                {src: 'img/webgallery/build_details.png'},
                {src: 'img/webgallery/build_outputs.png'},
                {src: 'img/webgallery/category_params.png'},
                {src: 'img/webgallery/category_subcats.png'},
                {src: 'img/webgallery/manufacturers.png'},
                {src: 'img/webgallery/part_category.png'},
                {src: 'img/webgallery/part_stock.png'},
                {src: 'img/webgallery/part_suppliers.png'},
              ]}
              options={{
                width: '80%',
              }}
            />}
        <ProjectStats />
      </main>
    </Layout>
  );
}
