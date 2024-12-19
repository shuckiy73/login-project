import React from "react";
import { useState } from "react";
import { Container, Row, Col, NavLink } from "react-bootstrap";
import { Link, useResolvedPath } from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';  
import { Form, Button } from "react-bootstrap";
import { ajax } from 'rxjs/ajax'
import './Signin.css';
import TopPanda from '../assets/img/top-panda.png'
import BottomPanda from '../assets/img/bottom-panda.png';
import axios from "axios";
import { FaTwitter, FaDiscord, FaFacebookF, FaTelegramPlane, FaInstagram} from "react-icons/fa";

// const AcceptLogin = ({ props }) => {
    
// }
function Signin({loginFlag}) {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [loginError, setError] = useState(false)
    
    const AcceptUser = () => {
        if(username === "" || password === ""){
            setError(true)
            return
        }
        axios
            .post("/api/acceptUser", {
                username: username,
                password: password
            })
            .then((response) => {
                if(response.data === "Faild")
                    setError(true)
                else{
                    setError(false)
                    loginFlag(true)
                }
            })
            .catch(err => console.log(err));
    }
    return(
        <div className="Signin">
            <Container className="Contain mb-4">
                <Row>
                    <Col sm="0" md="4"/>
                    <Col xs="12" sm="12" md="4">
                    <div className="Top-Panda"><img className="Topimg" src={TopPanda} alt="Lorewave"/></div>
                        <Form className="Signin-From pt-5">
                            <Form.Group className="mb-3" controlId="formBasicEmail">
                                <Form.Control type="email" placeholder="Enter email" value={username} onChange={(e) => {
                                    setUsername(e.target.value)
                                }}/>
                                {/* <Form.Text className="Valid-Gmail Valid-Label">
                                    We'll never share your email with anyone else.
                                </Form.Text> */}
                            </Form.Group>
                            <Form.Group className="mb-3" controlId="formBasicPassword mt-2">
                                <Form.Control type="password" placeholder="Password" vlaue={password} onChange={(e) => {
                                    setPassword(e.target.value)
                                }}/>
                                {/* <Form.Text className="Valid-Pass Valid-Label">
                                    We'll never share your email with anyone else.
                                </Form.Text> */}
                            </Form.Group>
                            <Button className="signin-button" onClick={AcceptUser}>
                                Signin
                                {/* {!loginLoading ? 'Sign In' : 'Logged in...'} */}
                                {/* <Link to="/welcome">SIGN IN</Link> */}
                            </Button>
                            {loginError && (
                                <div className="alert alert-danger mt-3">
                                Bad combination of username and password.
                                </div>
                            )}
                            <div className="Footer-main-community mt-3">
                                <NavLink href="" target="_blank"><FaInstagram/></NavLink>
                                <NavLink href="" target="_blank"><FaTwitter/></NavLink>
                                <NavLink href="" target="_blank"><FaFacebookF/></NavLink>
                            </div>
                        </Form>
                    </Col>
                </Row>
            </Container>
            <div className="Bottom-Panda"><img className="Bottomimg" src={BottomPanda} alt="Bottomimg"/></div>
        </div>
    );
}
export default Signin;