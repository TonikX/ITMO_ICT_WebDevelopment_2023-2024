# Задание №4

Реализуем отображение лидерборда во фронтенде посредством React.js

## Клиент (panels/rating/index.tsx):

```typescript
import React, { useState, useEffect } from "react";
import styled from "@emotion/styled";
import { Panel, Button, Placeholder } from "@vkontakte/vkui";

import Balance from "@/components/Balance";
import { request } from "@/utils/request";
import bridge from "@vkontakte/vk-bridge";
import { Icon56UserBookOutline, Icon56UsersOutline } from "@vkontakte/icons";

import Tabbar from "./Tabbar";
import Item from "./Item";
import List from "./List";
import Banner from "./Banner";

import "./types.d.ts";
import { images } from "@/data/url";
import { getAppId } from "@/utils/getAppId";

const Root = styled(Panel)({
  height: "100%",
  backgroundImage: `url(${images.background.rating})`,
  backgroundSize: "contain",
  "& > div": {
    height: "100%",
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
    alignItems: "center",
    padding: "0 8px",
    backgroundColor: "transparent !important",
  },
  "&:after": {
    backgroundColor: "transparent !important",
  },
});

const Card = styled("div")({
  height: "100%",
  overflowY: "auto",
  position: "relative",
  borderRadius: 14,
  background: "#EFF8FD",
  width: "100%",
  display: "flex",
  flexDirection: "column",
  boxShadow: "0 3px 0 0 rgba(255, 255, 255, 0.5)",
});

const ContentWrapper = styled.div`
  padding: 16px 8px;
  padding-top: 62px;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 18px;
  max-width: 450px;
`;

const UserPlacement = styled.div`
  position: sticky;
  left: 0;
  right: 0;
  bottom: 0;
  background: #f8fcff;
  box-shadow: 0px -2px 0px rgba(0, 0, 0, 0.05);
  z-index: 1;
  padding: 8px;
`;

const RatingPanel: React.FC<{ id: string }> = () => {
  const [globalRating, setGlobalRating] = useState<IRatingState>();
  const [friendsRating, setFriendsRating] = useState<IRatingState>();
  const [season, setSeason] = useState<{ banner?: IBanner }>({});

  const [activeTabIndex, setActiveTabIndex] = useState(0);
  const rating = activeTabIndex === 0 ? globalRating : friendsRating;

  const appId = getAppId();

  // Добавляем к аватарам пользователей приз (стикерпак), который пользователь может получить если займет призовое место в лидерборде
  const fillUsersFields = (items: ServerRatingItem[]) => {
    items.forEach((user: RatingItem) => {
      user.isStickersShow =
        activeTabIndex === 0 &&
        (season?.banner?.stickers || 0) + 1 > user.position;
    });
  };

  // Запрашиваем access_token пользователя через vk bridge, чтобы получить доступ к списку его друзей
  const getAccessToken = async (
    scope: string
  ): Promise<
    | { access_token: string; error?: undefined }
    | { error: true; access_token?: undefined }
  > => {
    try {
      const access_token = await bridge.send("VKWebAppGetAuthToken", {
        app_id: appId,
        scope,
      });
      return { access_token: access_token.access_token };
    } catch (err) {
      return { error: true };
    }
  };

  // Запрашиваем данные для рейтинга друзей пользователя
  const getFriendsRating = async () => {
    setFriendsRating(undefined);

    const { access_token, error } = await getAccessToken("friends");
    if (error) return setFriendsRating({ error: "access_error_friends" });

    let { response: list } = await bridge.send("VKWebAppCallAPIMethod", {
      method: "friends.getAppUsers",
      params: { access_token, v: "5.131" },
    });
    list = list.join(",");

    // Отправляем запрос на бекенд для получения списка друзей
    const res = (await request({
      method: "user/friendsRating",
      auth: true,
      params: { list },
    })) as IResponse | { error: "no_friends" };

    setFriendsRating(res as IRatingState);
  };

  // Запрашиваем актуальный список рейтинга
  const fetchCurrentRating = async () => {
    if (activeTabIndex === 0) {
      const res = (await request({
        method: "user/rating",
        auth: true,
      })) as IResponse;

      fillUsersFields([...res.items, res.user]);
      setGlobalRating(res as IRatingState);
      return;
    }

    getFriendsRating();
  };

  // Запрашиваем информацию о проходящем сейчас сезоне (если есть)
  useEffect(() => {
    (async () => {
      const seasonData = (await request({
        method: "user/season",
        auth: true,
      })) as { banner?: IBanner };
      if (seasonData.banner) seasonData.banner.endsAt += Date.now();

      setSeason(seasonData.banner ? seasonData : { banner: null });
    })();
  }, []);

  useEffect(() => {
    if (rating || (!season.banner && season.banner !== null)) return;
    fetchCurrentRating();
  }, [season, activeTabIndex]);

  return (
    <Root>
      <Balance />

      <ContentWrapper>
        {season.banner && <Banner data={season.banner} />}

        <Card>
          <Tabbar
            tabs={["Общий", "Друзья"]}
            activeTabIndex={activeTabIndex}
            setActiveTabIndex={setActiveTabIndex}
          />
          {!rating?.error && (
            <>
              <List data={rating?.items} season={season} />
              {rating?.user && (
                <UserPlacement>
                  <Item data={rating?.user} />
                </UserPlacement>
              )}
            </>
          )}

          {rating?.error === "access_error_friends" && (
            <Placeholder
              icon={<Icon56UsersOutline />}
              header="Нет доступа"
              stretched
              action={
                <Button size="s" onClick={fetchCurrentRating}>
                  Разрешить
                </Button>
              }
            >
              Разрешите приложению
              <br />
              получить список ваших друзей
            </Placeholder>
          )}

          {rating?.error === "no_friends" && (
            <Placeholder icon={<Icon56UserBookOutline />} stretched>
              Ваших друзей пока нет в приложении,
              <br /> но вы можете пригласить их!
            </Placeholder>
          )}
        </Card>
      </ContentWrapper>
    </Root>
  );
};

export default React.memo(RatingPanel);
```
