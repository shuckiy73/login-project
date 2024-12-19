import React from 'react';
import './Header.css';  
import { Button } from 'react-bootstrap';
import { Container, Nav, Navbar } from "react-bootstrap";
// import Logo from '../../assets/img/Logo_LepreCons_Finales.png';

function Header({ loginFlag }) {
  return (
    <div className="Header">
      <Navbar collapseOnSelect expand="sm">
        <Container>
          <Navbar.Brand href="">Лого</Navbar.Brand>
          <Navbar.Toggle aria-controls="responsive-navbar-nav" sx={{ color: 'white' }} />
          <Navbar.Collapse id="responsive-navbar-nav">
            <Nav className="me-auto">
              <Nav.Link href="">О НАС</Nav.Link>
              <Nav.Link href="">ИСТОРИЯ</Nav.Link>
              <Nav.Link href="">ОСОБЕННОСТИ</Nav.Link>
              <Nav.Link href="">ПЛАН</Nav.Link>
              <Nav.Link href="">КОМАНДА</Nav.Link>
              <Nav.Link href="">ВОПРОСЫ</Nav.Link>
              <Nav.Link href="">
                <Button 
                  style={{ height: 30, paddingTop: 1 }} 
                  onClick={(event) => {
                    loginFlag(false)
                  }}
                >
                  ВЫЙТИ
                </Button>
              </Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
    </div>
  );
}

export default Header;