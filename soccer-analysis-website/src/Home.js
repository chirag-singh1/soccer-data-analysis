import './Home.css';
import lead_graphic from './assets/img/lead_graphic.png';
import placeholder from './assets/img/placeholder.PNG';
import spain_portugal_thumbnail from './assets/img/spain_portugal_thumbnail.jpg';
import { Link } from 'react-router-dom';

export default function Home(){
    return (
        <div class='Home'>
            <div class='content'>
            <h1 class='WebsiteTitle'>Analyzing Soccer: A Data Driven Approach</h1>
            <div class='AboutBar'>
                <div class='AboutText'>
                    <h2 class='AboutTitle'>About this Project</h2>
                    <p class='AboutText'>This project is a compilation of analysis done on a public dataset created in 2019 by Wyscout and University of Pisa researchers. 
                    The content of the dataset was parsed using a variety of Python scripts to generate processed JSON objects to be displayed as graphs. 
                    The scripts used to generate all of the necessary JSON files displayed, generated JSON files, and the source code for this website can all 
                    be found in the project Github repository.
                    </p>
                    <Link to='/about'> <button class='AboutButton'>More Development Info &nbsp;<i class='arrow'></i></button></Link>
                    <a href='https://github.com/chirag-singh1/soccer-data-analysis'> <button class='AboutButton'>View Project Repository &nbsp;<i class='arrow'></i></button></a>
                    <a href='https://forms.gle/NqGGq9uoCxyfrrFXA'> <button class='AboutButton'>Suggest a Topic &nbsp;<i class='arrow'></i></button></a>
                </div>
                <img class='AboutImage' src={placeholder}></img>
            </div>
            <h2 class='ArticlesTitle'>Recent Features:</h2>
            <div class='Articles'>
                <a class='ArticleLink' href='/articles/lead'>
                    <div class='ArticleFeature'>
                        <h4 class='ArticleFeatureTitle'>Is 2-0 really the most dangerous lead?</h4>
                        <img class='FeatureArticleThumbnail' src={lead_graphic}></img>
                        <p class='FeatureArticleDescription'>An in-depth look at one of soccer's most famous myths, analyzing the attacking patterns of leading
                        and trailing teams by deficit</p>
                    </div>
                </a>
                <a class='ArticleLink' href='/articles/spain-portugal'>
                    <div class='ArticleFeature'>
                        <h4 class='ArticleFeatureTitle'>Spain and Portugal's 3 - 3 World Cup Draw</h4>
                        <img class='FeatureArticleThumbnail' src={spain_portugal_thumbnail}></img>
                        <p class='FeatureArticleDescription'>Revisiting one of the most iconic World Cup group stage matches through the buildup to each of the 6 goals</p>
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
            <div class='footer'>
                <p>Photos courtesy of AFP</p>
            </div>

            </div>
        </div>
    );
}