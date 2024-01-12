# База данных

Так как лабораторные 2 и 3 были сданы в виде другого проекта, реализацию бекенда проекта следует начать с самого начала: реализации схемы БД.

### Схема устройства

```typescript
export enum DeviceType {
  LIGHT_BULB = 'light_bulb',
  KETTLE = 'kettle',
  THERMOSTAT = 'thermostat',
  CAMERA_OUTDOOR = 'camera_outdoor',
}

export enum DeviceState {
  ONLINE,
  OFFLINE,
}

export enum DeviceCapabilityType {
  COLOR_SETTING = 'color_setting',
  ON_OFF = 'on_off',
  RANGE = 'range',
  VIDEO_STREAM = 'video_stream',
}

export interface BasicDevice {
  id: string
  userId: string
  name: string
  state: DeviceState
  favorite: boolean
  type: DeviceType
  capabilities: {
    [Type in DeviceCapabilityType]?: DeviceCapabilityByType<Type>
  }
}
```

В приведённом выше коде показано, как формируется тип “базового” умного устройства. Ему задан уникальный ID, имя, состояние онлайн/оффлайн и набор способностей. В данный момент поддерживается четыре способности для устройства:
- COLOR_SETTING – управление цветом в hsv
- ON_OFF – переключатель вкл/выкл
- RANGE – переключение по заданному промежутку с определённым шагом
- VIDEO_STREAM – стриминг видео, например, с наружней камеры

В приложении реализована поддержка четырех устройств: лампочка, термостат, чайник и камера. Но, с помощью такой структуры с использованием способностей, можно реализовать поддержку множества умных устройств, так как их возможности зачастую сводятся к этому набору из четырех способностей.

### MongoDB

Схема устройства для `mongodb`:

```typescript
// src/devices/schemas/device.schema.ts
import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose'
import mongoose, { HydratedDocument } from 'mongoose'
import {
  DeviceCapabilityType,
  DeviceCapabilityByType,
  DeviceType,
} from '@smart-home/shared'

export type DeviceDocument = HydratedDocument<Device>

@Schema()
export class Device {
  @Prop({ required: true })
  name: string

  @Prop({
    required: true,
    enum: Object.values(DeviceType),
  })
  type: `${DeviceType}`

  @Prop({ required: true })
  state: 0 | 1

  @Prop({ required: false, default: false })
  favorite: boolean

  @Prop({ type: mongoose.Schema.Types.ObjectId })
  userId: string

  @Prop({ required: true, type: mongoose.Schema.Types.Mixed })
  capabilities: {
    [Type in DeviceCapabilityType]?: DeviceCapabilityByType<Type>
  }
}

export const DeviceSchema = SchemaFactory.createForClass(Device)
```

### Схема пользователя

```typescript
// src/user/schemas/user.schema.ts
import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose'
import { HydratedDocument } from 'mongoose'
import * as mongoose from 'mongoose'
import { Device } from '../../devices/schemas/device.schema'

export type UserDocument = HydratedDocument<User>

@Schema()
export class User {
  @Prop({ required: true })
  fullname: string

  @Prop({ required: false })
  avatarUrl?: string

  @Prop({ required: true })
  email: string

  @Prop({ required: true })
  password: string

  @Prop({ type: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Device' }] })
  devices: Device[]

  @Prop()
  refreshToken: string
}

export const UserSchema = SchemaFactory.createForClass(User)
```
