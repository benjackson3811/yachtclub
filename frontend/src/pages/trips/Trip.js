import React from "react";
import styles from "../../styles/Trip.module.css";
import { useCurrentUser } from "../../contexts/CurrentUserContext";
import { Card, Media, OverlayTrigger, Tooltip } from "react-bootstrap";
import { Link, useHistory } from "react-router-dom";
import Avatar from "../../components/Avatar";
import { axiosRes } from "../../api/axiosDefaults";
import { MoreDropdown } from "../../components/MoreDropdown";

const Trip = (props) => {
  const {
    id,
    user,
    profile_id,
    profile_avatar,
    comments_count,
    likes_count,
    like_id,
    trip_title,
    description,
    image,
    updated_at,
    tripPage,
    setTrips,
  } = props;

  const currentUser = useCurrentUser();
  const is_user = currentUser?.username === user;
  const history = useHistory();

  const handleEdit = () => {
    history.push(`/trips/${id}/edit`);
  };

  const handleDelete = async () => {
    try {
      await axiosRes.delete(`/trips/${id}/`);
      history.goBack();
    } catch (err) {
      console.log(err);
    }
  };

  const handleLike = async () => {
    try {
      const { data } = await axiosRes.post("/likes/", { trip: id });
      setTrips((prevTrips) => ({
        ...prevTrips,
        results: prevTrips.results.map((trip) => {
          return trip.id === id
            ? { ...trip, likes_count: trip.likes_count + 1, like_id: data.id }
            : trip;
        }),
      }));
    } catch (err) {
      console.log(err);
    }
  };

  const handleUnlike = async () => {
    try {
      await axiosRes.delete(`/likes/${like_id}/`);
      setTrips((prevTrips) => ({
        ...prevTrips,
        results: prevTrips.results.map((trip) => {
          return trip.id === id
            ? { ...trip, likes_count: trip.likes_count - 1, like_id: null }
            : trip;
        }),
      }));
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <Card className={styles.trip}>
      <Card.Body>
        <Media className="align-items-center justify-content-between">
          <Link to={`/profiles/${profile_id}`}>
            <Avatar src={profile_avatar} height={45} />
            {user}
          </Link>
          <div className="d-flex align-items-center">
            <span>{updated_at}</span>
            {is_user && tripPage && (
              <MoreDropdown
                handleEdit={handleEdit}
                handleDelete={handleDelete}
              />
            )}
          </div>
        </Media>
      </Card.Body>
      <Link to={`/trips/${id}`}>
        <Card.Img src={image} alt={trip_title} />
      </Link>
      <Card.Body>
        {trip_title && <Card.Title className="text-center">{trip_title}</Card.Title>}
        {description && <Card.Text>{description}</Card.Text>}
        <div className={styles.TripBar}>
          {is_user ? (
            <OverlayTrigger
              placement="top"
              overlay={<Tooltip>You can't like your own trip!</Tooltip>}
            >
              <i className="far fa-heart" />
            </OverlayTrigger>
          ) : like_id ? (
            <span onClick={( handleUnlike )}>
              <i className={`fas fa-heart ${styles.Heart}`} />
            </span>
          ) : currentUser ? (
            <span onClick={( handleLike )}>
              <i className={`far fa-heart ${styles.HeartOutline}`} />
            </span>
          ) : (
            <OverlayTrigger
              placement="top"
              overlay={<Tooltip>Log in to like a trip!</Tooltip>}
            >
              <i className="far fa-heart" />
            </OverlayTrigger>
          )}
          {likes_count}
          <Link to={`/trips/${id}`}>
            <i className="far fa-comments" />
          </Link>
          {comments_count}
        </div>
      </Card.Body>
    </Card>
  );
};

export default Trip;