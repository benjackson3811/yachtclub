import React, { useEffect, useState } from "react";

import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import Container from "react-bootstrap/Container";

import appStyles from "../../App.module.css";
import { useParams } from "react-router-dom/cjs/react-router-dom.min";
import { axiosReq } from "../../api/axiosDefaults";
import Trip from "./Trip";

import CommentCreateForm from "../comments/CommentCreateForm";
import { useCurrentUser } from "../../contexts/CurrentUserContext";
import { Comment } from "../comments/Comment";

function TripPage() {
  const { id } = useParams();
  const [ trip, setTrip ] = useState({ results: [] });

  const currentUser = useCurrentUser();
  const profile_avatar = currentUser?.profile_avatar;
  const [comments, setComments] = useState({ results: [] });

  useEffect(() => {
    const handleMount = async () => {
      try {
        const [{ data: trip }, {data: comments}] = await Promise.all([
          axiosReq.get(`/trips/${id}`),
          axiosReq.get(`/comments/?trip=${id}`)
        ]);
        setTrip({ results: [trip] });
        setComments(comments);
      } catch (err) {
        console.log (err) ;
      }
    };
    handleMount();
  }, [id]);

  return (
    <Row className="h-100">
      <Col className="py-2 p-0 p-lg-2" lg={8}>
        <p>Popular profiles for mobile</p>
        <Trip {...trip.results[0]} setTrips={setTrip} tripPage />
        <Container className={appStyles.Content}>
          {currentUser ? (
            <CommentCreateForm
              profile_id={currentUser.profile_id}
              profileAvatar={profile_avatar}
              post={id}
              setTrip={setTrip}
              setComments={setComments}
            />
          ) : comments.results.length ? (
            "Comments"
          ) : null}
          {comments.results.length ? (
            comments.results.map(comment => (
              <Comment key={comment.id} {...comment}/>
            ))
          ) : currentUser ? (
            <span>No comments yet, be the first to comment!</span>
          ) : (
            <span>No comments... yet</span>
          )}

        </Container>
      </Col>
      <Col lg={4} className="d-none d-lg-block p-0 p-lg-2">
        Popular profiles for desktop
      </Col>
    </Row>
  );
}

export default TripPage;