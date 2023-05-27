"use client";
import NextLink from "next/link";
import { Button, Link as MuiLink } from "@mui/material";

const page = () => {
  return (
    <NextLink href="/" passHref>
      <Button variant="contained">ホーム</Button>
    </NextLink>
  );
};

export default page;
