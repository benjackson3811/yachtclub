import React, { useEffect, useState } from "react";

import Form from "react-bootstrap/Form";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import Container from "react-bootstrap/Container";

import Trip from "./Trip";
import Asset from "../../components/Asset";

import appStyles from "../../App.module.css";
import styles from "../../styles/TripsPage.module.css";
import { useLocation } from "react-router-dom";
import { axiosReq } from "../../api/axiosDefaults";

import NoResults from "../../assets/no-results.png";
import InfiniteScroll from "react-infinite-scroll-component";
import { fetchMoreData } from "../../utils/utils";

function TripsPage({ message, filter = "" }) {
  const [trips, setTrips] = useState({ results: [] });
  const [hasLoaded, setHasLoaded] = useState(false);
  const { pathname } = useLocation();

  const [query, setQuery] = useState("");

  useEffect(() => {
    const fetchTrips = async () => {
      try {
        const { data } = await axiosReq.get(`/trips/?${filter}search=${query}`);
        setTrips(data);
        setHasLoaded(true);
      } catch (err) {
        console.log(err);
      }
    };

    setHasLoaded(false);
    const timer = setTimeout(() => {
        fetchTrips();
    }, 1000)
    return () => {
        clearTimeout(timer);
    }
  }, [filter, query, pathname]);
  
  return (
    <Row className="h-100">
      <Col className="py-2 p-0 p-lg-2" lg={8}>
        <p>Popular profiles mobile</p>
        <i className={`fas fa-search ${styles.SearchIcon}`} />
        <Form
          className={styles.SearchBar}
          onSubmit={(event) => event.preventDefault()}
        >
          <Form.Control
            value={query}
            onChange={(event) => setQuery(event.target.value)}
            type="text"
            className="mr-sm-2"
            placeholder="Search trips"
          />
        </Form>

        {hasLoaded ? (
          <>
            {trips.results.length ? (
              <InfiniteScroll
                children={trips.results.map((trip) => (
                <Trip key={trip.id} {...trip} setTrips={setTrips} />
              ))}
                dataLength={trips.results.length}
                loader={<Asset spinner />}
                hasMore={!!trips.next}
                next={() => fetchMoreData(trips, setTrips)}
              />
            ) : (
              <Container className={appStyles.Content}>
                <Asset src={NoResults} message={message} />
              </Container>
            )}
          </>
        ) : (
          <Container className={appStyles.Content}>
            <Asset spinner />
          </Container>
        )}
      </Col>
      <Col md={4} className="d-none d-lg-block p-0 p-lg-2">
        <p>Popular profiles for desktop</p>
      </Col>
    </Row>
  );
}

export default TripsPage;
