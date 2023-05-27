"use client";
import NextLink from "next/link";
import { Button, Link as MuiLink } from "@mui/material";

const Home = () => {
  return (
    <NextLink href="/user_profile" passHref>
      <Button variant="contained">ユーザープロフィール</Button>
    </NextLink>
  );
};

export default Home;
