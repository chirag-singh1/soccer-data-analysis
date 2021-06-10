import './Home.css';
import lead_graphic from './assets/img/lead_graphic.png';
import placeholder from './assets/img/placeholder.PNG';

export default function Home(){
    return (
        <div class='Home'>
            <h1 class='WebsiteTitle'>Analyzing Soccer: A Data Driven Approach</h1>
            <div class='Articles'>
                <a class='ArticleLink' href='/articles/lead'>
                    <div class='ArticleFeature'>
                        <h4 class='ArticleFeatureTitle'>Is 2-0 really the most dangerous lead?</h4>
                        <img class='FeatureArticleThumbnail' src={lead_graphic}></img>
                        <p class='FeatureArticleDescription'>An in-depth look at one of soccer's most famous myths, analyzing the attacking patterns of leading
                        and trailing teams by deficit</p>
                    </div>
                </a>
                <a class='ArticleLink' href='/articles/league-defending'>
                    <div class='ArticleFeature'>
                        <h4 class='ArticleFeatureTitle'>Is 2-0 really the most dangerous lead?</h4>
                        <img class='FeatureArticleThumbnail' src={placeholder}></img>
                        <p class='FeatureArticleDescription'>An in-depth look at one of soccer's most famous myths, analyzing the attacking patterns of leading
                        and trailing teams by deficit</p>
                    </div>
                </a>
                <a class='ArticleLink' href='/articles/league-defending'>
                    <div class='ArticleFeature'>
                        <h4 class='ArticleFeatureTitle'>Is 2-0 really the most dangerous lead?</h4>
                        <img class='FeatureArticleThumbnail' src={placeholder}></img>
                        <p class='FeatureArticleDescription'>An in-depth look at one of soccer's most famous myths, analyzing the attacking patterns of leading
                        and trailing teams by deficit MORE TEXT AAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAA AAAAAAAAAAAA AAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAA</p>
                    </div>
                </a>
                <a class='ArticleLink' href='/articles/league-defending'>
                    <div class='ArticleFeature'>
                        <h4 class='ArticleFeatureTitle'>Is 2-0 really the most dangerous lead?</h4>
                        <img class='FeatureArticleThumbnail' src={placeholder}></img>
                        <p class='FeatureArticleDescription'>An in-depth look at one of soccer's most famous myths, analyzing the attacking patterns of leading
                        and trailing teams by deficit MORE TEXT AAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAA AAAAAAAAAAAA AAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAA</p>
                    </div>
                </a>
                <a class='ArticleLink' href='/articles/league-defending'>
                    <div class='ArticleFeature'>
                        <h4 class='ArticleFeatureTitle'>Is 2-0 really the most dangerous lead?</h4>
                        <img class='FeatureArticleThumbnail' src={placeholder}></img>
                        <p class='FeatureArticleDescription'>An in-depth look at one of soccer's most famous myths, analyzing the attacking patterns of leading
                        and trailing teams by deficit MORE TEXT AAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAA AAAAAAAAAAAA AAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAA</p>
                    </div>
                </a>
                <a class='ArticleLink' href='/articles/league-defending'>
                    <div class='ArticleFeature'>
                        <h4 class='ArticleFeatureTitle'>Is 2-0 really the most dangerous lead?</h4>
                        <img class='FeatureArticleThumbnail' src={placeholder}></img>
                        <p class='FeatureArticleDescription'>An in-depth look at one of soccer's most famous myths, analyzing the attacking patterns of leading
                        and trailing teams by deficit MORE TEXT AAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAA AAAAAAAAAAAA AAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAA</p>
                    </div>
                </a>
            </div>
        </div>
    );
}