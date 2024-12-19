import React from "react";
import { Container, Row, Col } from "react-bootstrap";
import 'bootstrap/dist/css/bootstrap.min.css';  
import { Form, Button } from "react-bootstrap";
import './Welcome.css';
import TopPanda from '../assets/img/top-panda.png'
import BottomPanda from '../assets/img/bottom-panda.png';
import Header from './Header.js'

function Welcome({ loginFlag }) {
    return (
        <div className="Welcome">
            <Header loginFlag={loginFlag} />
            <Container>
                <div className="Main-Text">
                    <h1>ДОБРО ПОЖАЛОВАТЬ</h1>
                    <div className="Line" />
                    <div className="Black-Text">
                        <h2>РАСПРОДАЖА ЧЕРНОЙ ПЯТНИЦЫ</h2>
                    </div>
                    <div className="Line1" />
                </div>
            </Container>
            <div className="Bottom-Panda"><img className="Bottomimg" src={BottomPanda} alt="Bottomimg" /></div>
        </div>
    );
}

export default Welcome;